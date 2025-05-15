import pickle
import random
import networkx as nx
from negative_sampler import NegativeSampler
import pandas as pd

class DataPrep:
    def __init__(self, graph_file, train_size=0.8, val_size=0.1):
        self.graph_file = graph_file
        self.train_size = train_size
        self.val_size = val_size
        self.edges = None
        self.all_nodes = None
        self.train_edges = None
        self.val_edges = None
        self.test_edges = None
        self.train_neg_samples = None
        self.val_neg_samples = None
        self.test_neg_samples = None
        self.deepwalk_graph = nx.Graph()


    def load_graph(self):
        with open(self.graph_file, "rb") as f:
            G = pickle.load(f)
        return G

    def train_test_val_split(self, random_state=42):
        G = self.load_graph()

        # Extract edges with relations
        self.edges = [(str(u), data['relation'], str(v)) for u, v, data in G.edges(data=True)]

        # Get all unique nodes
        self.all_nodes = sorted(list(set(G.nodes())))

        random.seed(random_state)
        random.shuffle(self.edges)

        # Train/Validation/Test Split
        total_edges = len(self.edges)
        train_size = int(self.train_size * total_edges)
        val_size = int(self.val_size * total_edges)

        self.train_edges = self.edges[:train_size]
        self.val_edges = self.edges[train_size:train_size + val_size]
        self.test_edges = self.edges[train_size + val_size:]
        
        print(" Split Sizes:")
        print(f"Total Edges: {total_edges}")
        print(f"Training Set: {len(self.train_edges)}")
        print(f"Validation Set: {len(self.val_edges)}")
        print(f"Test Set: {len(self.test_edges)}")

        return G, self.train_edges, self.val_edges, self.test_edges, self.all_nodes
    

    def negative_sampling(self, G, train_edges, val_edges, test_edges, all_nodes, random_state=42):
        # Negative Sampling
        sampler = NegativeSampler(edges=train_edges, all_nodes=all_nodes, random_state=random_state)

        train_neg_samples = sampler.generate_negative_samples(len(train_edges))
        val_neg_samples = sampler.generate_negative_samples(len(val_edges))
        test_neg_samples = sampler.generate_negative_samples(len(test_edges))

        print("\n Negative Sample Sizes:")
        print(f"Train Negatives: {len(train_neg_samples)}")
        print(f"Validation Negatives: {len(val_neg_samples)}")
        print(f"Test Negatives: {len(test_neg_samples)}")

        return train_neg_samples, val_neg_samples, test_neg_samples

    def save_deepwalk_graph(self, G, train_edges, graph_name):

        for h, r, t in train_edges:
            self.deepwalk_graph.add_edge(str(h), str(t), relation=str(r))

            # if 'relations' not in self.deepwalk_graph.nodes[str(h)]:
            #     self.deepwalk_graph.nodes[str(h)]['relations'] = set()
            # self.deepwalk_graph.nodes[str(h)]['relations'].add(r)
            
        # for n in self.deepwalk_graph.nodes:
        #     if 'relations' in self.deepwalk_graph.nodes[str(n)]:
        #         self.deepwalk_graph.nodes[str(n)]['relations'] = list(self.deepwalk_graph.nodes[str(n)]['relations'])

        nx.write_gpickle(self.deepwalk_graph, graph_name)
        print(f"\n DeepWalk graph saved as {graph_name}")
        # print(deepwalk_graph.nodes(data=True))

    def get_ground_truth(self, file_name):
        gt = pd.read_csv(file_name)
        def generate_IRI(book_name):
            return f"""https://koncordantlab.com/TTEXTS/book/{book_name.strip().lower().replace("'", "").replace(' ', '_').replace('-', '')}"""
        ground_truth = {}
        for i, row in gt.iterrows():
            ground_truth[generate_IRI(row['Book_name'])] = [generate_IRI(row['1st Recommendation']), generate_IRI(row['2nd Recommendation']), generate_IRI(row['3rd Recommendation']), generate_IRI(row['4th Recommendation']), generate_IRI(row['5th Recommendation'])]  
        return ground_truth

if __name__ == "__main__":
    prep = DataPrep(graph_file="./data/graph.gpickle")
    G, train_edges, val_edges, test_edges, all_nodes = prep.train_test_val_split()
    train_neg_samples, val_neg_samples, test_neg_samples = prep.negative_sampling(G, train_edges, val_edges, test_edges, all_nodes)
    prep.save_deepwalk_graph(G, train_edges, '"./data/deepwalk_graph.gpickle"')


    # print(prep.get_ground_truth("./data/ground_truth.csv"))

   