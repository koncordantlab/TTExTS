import random
from gensim.models import Word2Vec
import pickle

class DeepwalkTrainer:
    def __init__(self, graph, walk_length=30, num_walks=10, dimensions=64, window_size=5, workers=4):
        """
        Initialize the DeepWalkTrainer with parameters for random walks and embedding training.

        :param graph: NetworkX graph object
        :param walk_length: Length of each random walk
        :param num_walks: Number of walks per node
        :param dimensions: Dimensions of the embedding vectors
        :param window_size: Context window size for Word2Vec
        :param workers: Number of worker threads for training
        """
        self.graph = graph
        self.walk_length = walk_length
        self.num_walks = num_walks
        self.dimensions = dimensions
        self.window_size = window_size
        self.workers = workers
    
    def generate_random_walks(self):
        """
        Generate random walks from the graph.

        :return: List of random walks
        """
        walks = []
        nodes = list(self.graph.nodes())
        for _ in range(self.num_walks):
            random.shuffle(nodes)
            for node in nodes:
                walks.append(self.random_walk(node))
        return walks

    def random_walk(self, start_node):
        """
        Perform a single random walk starting from a given node.

        :param start_node: Starting node for the walk
        :return: A single random walk (list of nodes)
        """
        walk = [start_node]
        for _ in range(self.walk_length - 1):
            cur = walk[-1]
            neighbors = list(self.graph.neighbors(cur))
            if neighbors:
                walk.append(random.choice(neighbors))
            else:
                break
        return walk

    def train_embeddings(self):
        """
        Train node embeddings using Word2Vec on random walks.

        :return: Trained Word2Vec model
        """
        walks = self.generate_random_walks()
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



if __name__=="__main__":
    with open('./data/deepwalk_graph.gpickle', "rb") as f:
        deepwalk_graph = pickle.load(f)

    trainer = DeepwalkTrainer(deepwalk_graph)
    print(trainer.generate_random_walks()[0])


