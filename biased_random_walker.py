import pickle
import random
import numpy as np
from gensim.models import Word2Vec

class BiasedRandomWalker:
    def __init__(self, graph, relation_weights, walk_length=10, num_walks=20,
                 dimensions=64, window_size=5, workers=1, seed=42):
        self.graph = graph
        self.relation_weights = relation_weights
        self.walk_length = walk_length
        self.num_walks = num_walks
        self.dimensions = dimensions
        self.window_size = window_size
        self.workers = workers
        self.seed = seed
        # Seeded random generators for reproducibility
        self.py_rng = random.Random(seed)
        self.np_rng = np.random.default_rng(seed)

    def weighted_choice(self, neighbors, relations):
        default_weight = min(self.relation_weights.values())
        weights = np.array(
            [self.relation_weights.get(rel, default_weight) for rel in relations],
            dtype=float
        )
        weights = weights / weights.sum()
        idx = self.np_rng.choice(len(neighbors), p=weights)
        return neighbors[idx]

    def biased_walk(self, start_node):
        walk = [start_node]
        for _ in range(self.walk_length - 1):
            current_node = walk[-1]
            # For MultiGraph, edges(node, data=True) yields every parallel edge
            edge_list = list(self.graph.edges(current_node, data=True))
            if not edge_list:
                break

            neighbors = [v for _, v, _ in edge_list]
            relations = [d.get('relation', 'None') for _, _, d in edge_list]

            # from collections import Counter
            # print("Relation Counts: ", Counter(relations))

            next_node = self.weighted_choice(neighbors, relations)
            walk.append(next_node)
        return walk

    def generate_walks(self):
        walks = []
        nodes = list(self.graph.nodes())
        for _ in range(self.num_walks):
            self.py_rng.shuffle(nodes)
            for node in nodes:
                walks.append(self.biased_walk(node))
        return walks

    def train_embeddings(self):
        walks = self.generate_walks()
        walks = [[str(node) for node in walk] for walk in walks]
        model = Word2Vec(
            sentences=walks,
            vector_size=self.dimensions,
            window=self.window_size,
            min_count=0,
            sg=1,
            workers=self.workers,
            seed=self.seed,
        )
        return model
    


if __name__ == "__main__":
    # Test BiasedRandomWalker
    import networkx as nx

    with open('./data/graphs/deepwalk_graph_351.gpickle', 'rb') as f:
        graph = pickle.load(f)

    # # Define relation weights
    relation_weights = {
        'https://koncordantlab.com/TTEXTS/has_genre': 3,
        'https://koncordantlab.com/TTEXTS/has_theme': 3,
        'https://koncordantlab.com/TTEXTS/has_subtheme': 3,
        'https://koncordantlab.com/TTEXTS/has_levels_of_meaning': 2,
        'https://koncordantlab.com/TTEXTS/has_text_structure': 2,
        'https://koncordantlab.com/TTEXTS/has_language_conventionality_and_clarity': 2,
        'https://koncordantlab.com/TTEXTS/has_knowledge_demands': 2,
        'Others': 1
    }

    walker = BiasedRandomWalker(graph, relation_weights, walk_length=10, num_walks=5, dimensions=16, window_size=3)
    walker.biased_walk('https://koncordantlab.com/TTEXTS/book/the_necklace')
    # model = walker.train_embeddings()
    # model.save('./data/biased_deepwalk.model')

    # print(list(graph.nodes)[:5])
    # print(graph['https://koncordantlab.com/TTEXTS/book/the_necklace']['https://koncordantlab.com/TTEXTS/Social_Status']['relation'])
   