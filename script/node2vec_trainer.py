from typing import Dict, List, Tuple, Any, Optional
import random
import numpy as np
import networkx as nx
from gensim.models import Word2Vec


def alias_setup(probs: List[float]) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute utility arrays for non-uniform sampling from discrete distributions.
    Returns:
        (J, q) as in the alias method
    """
    K = len(probs)
    q = np.array(probs, dtype=np.float64) * K
    J = np.zeros(K, dtype=np.int32)

    smaller = []
    larger = []

    for idx, prob in enumerate(q):
        if prob < 1.0:
            smaller.append(idx)
        else:
            larger.append(idx)

    while smaller and larger:
        small = smaller.pop()
        large = larger.pop()

        J[small] = large
        q[large] = q[large] - (1.0 - q[small])

        if q[large] < 1.0:
            smaller.append(large)
        else:
            larger.append(large)

    # leftover entries
    # J entries are already 0 where not set; q entries near 1
    return J, q


def alias_draw(J: np.ndarray, q: np.ndarray) -> int:
    """
    Draw sample from a non-uniform discrete distribution using alias tables.
    """
    K = len(J)
    kk = int(np.floor(np.random.rand() * K))
    if np.random.rand() < q[kk]:
        return kk
    else:
        return J[kk]


class Node2Vec:
    def __init__(
        self,
        G: nx.Graph,
        dimensions: int = 128,
        walk_length: int = 80,
        num_walks: int = 10,
        window_size: int = 10,
        p: float = 1.0,
        q: float = 1.0,
        workers: int = 4,
        seed: Optional[int] = None,
    ):
        """
        G: networkx graph (can be directed)
        p, q: Node2Vec hyperparameters
        """
        self.G = G
        self.dimensions = dimensions
        self.walk_length = walk_length
        self.num_walks = num_walks
        self.window_size = window_size
        self.p = p
        self.q = q
        self.workers = workers
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)

        # alias sampling structures
        self.alias_nodes: Dict[Any, Tuple[np.ndarray, np.ndarray]] = {}
        self.alias_edges: Dict[Tuple[Any, Any], Tuple[np.ndarray, np.ndarray]] = {}

        self._preprocess_transition_probs()

    def _get_edge_weight(self, src: Any, dst: Any) -> float:
        data = self.G.get_edge_data(src, dst, default={})
        return float(data.get("weight", 1.0))

    def _preprocess_transition_probs(self):
        """
        Precompute alias tables for nodes and edges to allow O(1) sampling
        during walk generation.
        """
        # alias nodes: distribution over neighbors for each source node
        for node in self.G.nodes():
            neighbors = list(self.G.neighbors(node))
            if len(neighbors) == 0:
                # isolated node
                self.alias_nodes[node] = (np.array([], dtype=np.int32), np.array([]))
                continue
            unnormalized_probs = []
            for nbr in neighbors:
                unnormalized_probs.append(self._get_edge_weight(node, nbr))
            norm_const = float(sum(unnormalized_probs))
            normalized = [u / norm_const for u in unnormalized_probs]
            self.alias_nodes[node] = alias_setup(normalized)

        # alias edges: distribution for transition (prev -> curr) over curr's neighbors
        is_directed = self.G.is_directed()
        for edge in self._edge_iterator():
            src, dst = edge
            dst_neighbors = list(self.G.neighbors(dst))
            if len(dst_neighbors) == 0:
                self.alias_edges[(src, dst)] = (np.array([], dtype=np.int32), np.array([]))
                continue

            unnormalized_probs = []
            for dst_nbr in dst_neighbors:
                weight = self._get_edge_weight(dst, dst_nbr)
                # bias based on relation of dst_nbr to src
                if dst_nbr == src:
                    factor = 1.0 / self.p
                elif self.G.has_edge(dst_nbr, src):
                    # dst_nbr is adjacent to src (i.e., distance 1)
                    factor = 1.0
                else:
                    factor = 1.0 / self.q
                unnormalized_probs.append(weight * factor)

            norm_const = float(sum(unnormalized_probs))
            normalized = [u / norm_const for u in unnormalized_probs]
            self.alias_edges[(src, dst)] = alias_setup(normalized)

            # if undirected, also register reverse edge with same logic when iterating edges ensures both
            # For directed graphs we only register the provided direction.

    def _edge_iterator(self):
        """
        Yield edges as (src, dst) pairs for which to compute edge transition probabilities.
        For undirected graphs we compute for both directions.
        """
        if self.G.is_directed():
            for src, dst in self.G.edges():
                yield src, dst
        else:
            # undirected: compute for both directions
            for src, dst in self.G.edges():
                yield src, dst
                yield dst, src

    def _node_sample_neighbor(self, node: Any) -> Optional[Any]:
        """
        Sample a neighbor of node using alias table for nodes.
        Returns neighbor node id or None if node has no neighbors.
        """
        neighbors = list(self.G.neighbors(node))
        if not neighbors:
            return None
        J, q = self.alias_nodes[node]
        idx = alias_draw(J, q)
        return neighbors[idx]

    def _edge_sample_next(self, prev: Any, curr: Any) -> Optional[Any]:
        """
        Sample next node given previous (prev) and current (curr) using precomputed alias_edges.
        """
        neighbors = list(self.G.neighbors(curr))
        if not neighbors:
            return None
        key = (prev, curr)
        if key not in self.alias_edges:
            # fallback to uniform neighbor sampling
            return random.choice(neighbors)
        J, q = self.alias_edges[key]
        idx = alias_draw(J, q)
        return neighbors[idx]

    def _walk_from(self, start_node: Any) -> List[str]:
        """
        Simulate a single walk of length walk_length starting from start_node.
        Returns list of node ids as strings (suitable for Word2Vec).
        """
        walk = [start_node]
        while len(walk) < self.walk_length:
            curr = walk[-1]
            if len(walk) == 1:
                nxt = self._node_sample_neighbor(curr)
            else:
                prev = walk[-2]
                nxt = self._edge_sample_next(prev, curr)
            if nxt is None:
                break
            walk.append(nxt)
        # convert to strings for gensim Word2Vec compatibility
        return [str(n) for n in walk]

    def simulate_walks(self, shuffle: bool = True) -> List[List[str]]:
        """
        Simulate num_walks per node and return list of walks (each walk is a list of string node ids).
        """
        nodes = list(self.G.nodes())
        walks: List[List[str]] = []
        for walk_iter in range(self.num_walks):
            if shuffle:
                random.shuffle(nodes)
            for node in nodes:
                walk = self._walk_from(node)
                if walk:
                    walks.append(walk)
        return walks

    def train_embeddings(
        self,
        walks: Optional[List[List[str]]] = None,
        min_count: int = 0,
        sg: int = 1,
    ):
        """
        Learn embeddings using gensim Word2Vec. If walks not provided, will simulate them.

        Returns the gensim Word2Vec model (so caller can extract vectors via model.wv).
        """
        if Word2Vec is None:
            raise RuntimeError("gensim is required for learn_embeddings; please install gensim.")

        if walks is None:
            walks = self.simulate_walks()

        model = Word2Vec(
            sentences=walks,
            vector_size=self.dimensions,
            window=self.window_size,
            min_count=min_count,
            sg=sg,
            workers=self.workers,
        )
        return model


# Convenience function
def node2vec_embeddings(
    G: nx.Graph,
    dimensions: int = 128,
    walk_length: int = 80,
    num_walks: int = 10,
    p: float = 1.0,
    q: float = 1.0,
    workers: int = 1,
    window_size: int = 10,
    epochs: int = 1,
    seed: Optional[int] = None,
):
    """
    Quick helper to run node2vec end-to-end and return gensim Word2Vec model.
    """
    n2v = Node2Vec(G, dimensions=dimensions, walk_length=walk_length, num_walks=num_walks, p=p, q=q, workers=workers, seed=seed)
    walks = n2v.simulate_walks()
    model = n2v.train_embeddings(walks=walks, window_size=window_size, epochs=epochs, workers=workers)
    return model


if __name__ == "__main__":
    G = nx.karate_club_graph()
    n2v = Node2Vec(G, dimensions=64, walk_length=20, num_walks=10, p=1, q=1, workers=1, seed=42)
    walks = n2v.simulate_walks()
    print("Generated", len(walks), "walks. Example walk:", walks[0])
    model = n2v.train_embeddings(walks=walks)
    print("Embedding for node 0:", model.wv['0'][:6])