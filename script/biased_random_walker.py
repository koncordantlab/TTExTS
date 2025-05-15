import random
import numpy as np
from gensim.models import Word2Vec

class BiasedRandomWalker:
    def __init__(self, graph, relation_weights, walk_length=10, num_walks=20, dimensions=64, window_size=5, workers=4):
        """
        :param graph: NetworkX graph where edges have relation types
        :param relation_weights: Dictionary {relation_type: weight}
        :param walk_length: Number of steps per walk
        :param num_walks: Number of walks per node
        """
        self.graph = graph
        self.relation_weights = relation_weights
        self.walk_length = walk_length
        self.num_walks = num_walks
        self.dimensions = dimensions
        self.window_size = window_size
        self.workers = workers
    
    def weighted_choice(self, neighbors, relations):
        """Select next node based on relation weights."""
        default_weight = min(self.relation_weights.values()) # Default weight for unknown relations
        weights = np.array([self.relation_weights.get(rel, default_weight) for rel in relations])
        weights = weights/ weights.sum()  # Normalize probabilities
        return np.random.choice(neighbors, p=weights)

    def biased_walk(self, start_node):
        """Perform a single biased random walk."""
        walk = [start_node]
        for _ in range(self.walk_length - 1):
            current_node = walk[-1]
            neighbors = list(self.graph.neighbors(current_node))
            if not neighbors:
                break  # Stop if no neighbors
            
            relations = [self.graph[current_node][nbr].get('relation', 'None') for nbr in neighbors]

            # relations = self.graph.nodes(data=True)[current_node].get('relations', 'None')
            next_node = self.weighted_choice(neighbors, relations)
            walk.append(next_node)
        return walk
    
    def generate_walks(self):
        """Generate multiple random walks per node."""
        walks = []
        nodes = list(self.graph.nodes())
        for _ in range(self.num_walks):
            random.shuffle(nodes)
            for node in nodes:
                walks.append(self.biased_walk(node))
        return walks
    
    def train_embeddings(self):
        """
        Train node embeddings using Word2Vec on random walks.

        :return: Trained Word2Vec model
        """
        walks = self.generate_walks()
        walks = [[str(node) for node in walk] for walk in walks]  # Convert nodes to strings for Word2Vec
        model = Word2Vec(
            sentences=walks,
            size=self.dimensions,
            window=self.window_size,
            min_count=0,
            sg=1,
            workers=self.workers
        )
        return model
    


if __name__ == "__main__":
    # Test BiasedRandomWalker
    import networkx as nx

    with open('./data/deepwalk_graph.gpickle', 'rb') as f:
        graph = nx.read_gpickle(f)

    # # Define relation weights
    relation_weights = {
        'https://koncordantlab.com/TTEXTS/predicates/has_genre': 3,
        'https://koncordantlab.com/TTEXTS/predicates/has_theme': 3,
        'https://koncordantlab.com/TTEXTS/predicates/has_subtheme': 3,
        'https://koncordantlab.com/TTEXTS/predicates/has_levels_of_meaning': 2,
        'https://koncordantlab.com/TTEXTS/predicates/has_text_structure': 2,
        'https://koncordantlab.com/TTEXTS/predicates/has_language_conventionality_and_clarity': 2,
        'https://koncordantlab.com/TTEXTS/predicates/has_knowledge_demands': 2,
        'Others': 1
    }

    walker = BiasedRandomWalker(graph, relation_weights, walk_length=10, num_walks=5, dimensions=16, window_size=3)

    # model = walker.train_embeddings()
    # model.save('./data/biased_deepwalk.model')

    # print(list(graph.nodes)[:5])
    # print(graph['https://koncordantlab.com/TTEXTS/book/the_necklace']['https://koncordantlab.com/TTEXTS/Social_Status']['relation'])
   