import pickle
import random
import torch
import json
import networkx as nx
from negative_sampler import NegativeSampler
import pandas as pd
import pickle
from utils.utils import clean_text, get_device
from rdflib import Graph, RDF, Literal
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import MinMaxScaler
import logging

logger = logging.getLogger(__name__)



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
        self.deepwalk_graph = nx.MultiGraph()


    def load_graph(self):
        with open(self.graph_file, "rb") as f:
            G = pickle.load(f)
        return G

    def train_test_val_split(self, random_state=42):
        G = self.load_graph()

        # Extract edges with relations
        self.edges = [(u, data.get('relation'), v) for u, v, data in G.edges(data=True)]

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

        logger.info("Split Sizes:")
        logger.info(f"Total Edges: {total_edges}")
        logger.info(f"Training Set: {len(self.train_edges)}")
        logger.info(f"Validation Set: {len(self.val_edges)}")
        logger.info(f"Test Set: {len(self.test_edges)}")

        return G, self.train_edges, self.val_edges, self.test_edges, self.all_nodes
    

    def negative_sampling(self, train_edges, val_edges, test_edges, all_nodes, random_state=42):
        # Negative Sampling
        sampler = NegativeSampler(edges=train_edges, all_nodes=all_nodes, random_state=random_state)

        train_neg_samples = sampler.generate_negative_samples(len(train_edges))
        val_neg_samples = sampler.generate_negative_samples(len(val_edges))
        test_neg_samples = sampler.generate_negative_samples(len(test_edges))

        logger.info("\nNegative Sample Sizes:")
        logger.info(f"Train Negatives: {len(train_neg_samples)}")
        logger.info(f"Validation Negatives: {len(val_neg_samples)}")
        logger.info(f"Test Negatives: {len(test_neg_samples)}")

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

        with open(graph_name, "wb") as f:
            pickle.dump(self.deepwalk_graph, f)
        # nx.write_gpickle(self.deepwalk_graph, graph_name)
        logger.info(f"DeepWalk graph saved as {graph_name}")
        # print(deepwalk_graph.nodes(data=True))

    def get_ground_truth(self, file_name):
        gt = pd.read_csv(file_name)
        def generate_IRI(book_name):
            return f"""https://koncordantlab.com/TTEXTS/{clean_text(book_name)}"""
        ground_truth = {}
        for i, row in gt.iterrows():
            ground_truth[generate_IRI(row['Book_name'])] = [generate_IRI(row['1st Recommendation']), generate_IRI(row['2nd Recommendation']), generate_IRI(row['3rd Recommendation']), generate_IRI(row['4th Recommendation']), generate_IRI(row['5th Recommendation'])]  
        return ground_truth


class GNNDataPrep:
    def __init__(self, file_path='data/kg_for_gnn.ttl', model_path_name='data/sentence-transformers/all-MiniLM-L6-v2', test_ratio=0.1, val_ratio=0.1):
        self.file_path = file_path
        self.model_name = model_path_name
        self.device = get_device()
        self.graph = self.load_graph()
        self.sbert = self.load_bert_model()
        self.uri_to_id = {}
        self.node_features = {}
        self.entities = set()
        self.book_numeric_data = {}
        self.book_text_data = {}
        self.id_counter = 0
        self.rel_set = set()
        self.src, self.dst, self.etype = [], [], []
        self.edge_index = None
        self.edge_type = None
        self.rel2id = None
        self.test_ratio = test_ratio
        self.val_ratio = val_ratio
        self.train_triples = []
        self.val_triples = []
        self.test_triples = []
        self.book_numeric_predicates = {
            "has_atos_reading_level",
            "has_flesch_kincaid",
            "has_lexile_level",
            "has_pages",
            "has_year_of_publication"
        }
        self.book_text_predicates = {
            "has_summary",
            "has_reader_maturity"
        }

    def load_graph(self):
        """Load RDF graph from a file."""
        graph = Graph()
        graph.parse(self.file_path, format="turtle")
        return graph

    def load_bert_model(self):
        """Load a pre-trained SBERT model."""
        return SentenceTransformer(self.model_name)

    def process_book_features(self):
        """Preprocess the RDF graph to extract entities and their features."""

        entity_identifiers = ["book"]

        for s, p, o in self.graph:
            s_str, p_str = str(s), str(p)
            if any(kw in s_str for kw in entity_identifiers):
                if s not in self.uri_to_id:
                    self.uri_to_id[s] = self.id_counter
                    self.id_counter += 1
                self.entities.add(s)
                pred = p_str.split("/")[-1]
                if isinstance(o, Literal):
                    if pred in self.book_numeric_predicates:
                        self.book_numeric_data.setdefault(s, {})[pred] = float(o)
                    elif pred in self.book_text_predicates:
                        self.book_text_data.setdefault(s, {})[pred] = str(o)
        

    def process_node_features(self):
        """Create node features from numeric and text data."""


        # Normalize numeric values
        all_numeric = []
        for e in self.entities:
            all_numeric.append([
                self.book_numeric_data.get(e, {}).get(pred, 0.0)
                for pred in self.book_numeric_predicates
            ])

        scaler = MinMaxScaler()
        scaled_numeric = scaler.fit_transform(all_numeric)

        for idx, entity in enumerate(self.entities):
            numeric_vec = torch.tensor(scaled_numeric[idx], dtype=torch.float32, device=self.device)

            # Embed all text predicates
            text_embeds = []
            for pred in self.book_text_predicates:
                txt = self.book_text_data.get(entity, {}).get(pred, "")
                if txt:
                    emb = torch.tensor(self.sbert.encode(txt), dtype=torch.float32, device=self.device)
                else:
                    emb = torch.zeros(384, device=self.device)
                text_embeds.append(emb)

            full_vec = torch.cat([numeric_vec] + text_embeds, dim=0)
            self.node_features[self.uri_to_id[entity]] = full_vec


    def assign_ids_and_features(self):
        """Assign IDs to all nodes and create a tensor for node features."""

        for s, p, o in self.graph:
            if s not in self.uri_to_id.keys():
                self.uri_to_id[s] = self.id_counter
                self.id_counter += 1
            if o not in self.uri_to_id.keys() and not isinstance(o, Literal):
                self.uri_to_id[o] = self.id_counter
                self.id_counter += 1

    def get_node_uri(self, node_id):
        """Get the URI of a node given its ID."""
        self.process_book_features()
        self.process_node_features()

        for uri, nid in self.uri_to_id.items():
            if nid == node_id:
                return uri
        return None
    
    def get_node_id(self, uri):
        """Get the ID of a node given its URI."""
        self.process_book_features()
        self.process_node_features()

        return self.uri_to_id.get(uri, None)
    
    def get_uri_to_id(self):
        """Get the mapping of URIs to IDs."""
        self.process_book_features()
        self.process_node_features()

        return self.uri_to_id
    
    def save_uri_to_id(self, file_path='data/uri_to_id_default.json'):
        """Save the URI to ID mapping to a JSON file."""
        self.process_book_features()
        self.process_node_features()

        with open(file_path, 'w') as f:
            json.dump(self.uri_to_id, f)
        print(f"URI to ID mapping saved to '{file_path}' with {len(self.uri_to_id)} entries.")

    def split_triples(self):
        all_triples = []
        for s, p, o in self.graph:
            if not isinstance(o, Literal):
                all_triples.append((self.uri_to_id[s], self.rel2id[str(p)], self.uri_to_id[o]))
        
        random.shuffle(all_triples)
        total = len(all_triples)
        test_size = int(total * self.test_ratio)
        val_size = int(total * self.val_ratio)
        self.test_triples = all_triples[:test_size]
        self.val_triples = all_triples[test_size:test_size + val_size]
        self.train_triples = all_triples[test_size + val_size:]

    def create_edge_index_and_type(self):
        """Create edge_index and edge_type tensors from the graph."""
        

        for s, p, o in self.graph:
            self.rel_set.add(str(p))

        self.rel2id = {r: i for i, r in enumerate(sorted(self.rel_set))}

        for s, p, o in self.graph:
            if isinstance(o, Literal):
                continue
            self.src.append(self.uri_to_id[s])
            self.dst.append(self.uri_to_id[o])
            self.etype.append(self.rel2id[str(p)])

        self.edge_index = torch.tensor([self.src, self.dst], dtype=torch.long, device=self.device)
        self.edge_type = torch.tensor(self.etype, dtype=torch.long, device=self.device)

    def prepare_data(self):
        """Prepare the data for GNN training."""
        self.load_graph()
        self.load_bert_model()
        self.process_book_features()
        self.process_node_features()
        self.assign_ids_and_features()
        self.save_uri_to_id()
        self.create_edge_index_and_type()
        self.split_triples()

        # Convert node features to tensor
        num_nodes = len(self.uri_to_id)
        feature_dim = len(next(iter(self.node_features.values())))
        x = torch.zeros((num_nodes, feature_dim), dtype=torch.float32, device=self.device)

        for node_id, features in self.node_features.items():
            x[node_id] = features

        return x, self.edge_index, self.edge_type, self.rel2id, self.train_triples, self.val_triples, self.test_triples



if __name__ == "__main__":
    # prep = DataPrep(graph_file="./data/graph.gpickle")
    # G, train_edges, val_edges, test_edges, all_nodes = prep.train_test_val_split()
    # train_neg_samples, val_neg_samples, test_neg_samples = prep.negative_sampling(G, train_edges, val_edges, test_edges, all_nodes)
    # prep.save_deepwalk_graph(G, train_edges, '"./data/deepwalk_graph.gpickle"')


    # print(prep.get_ground_truth("./data/ground_truth.csv"))

    data_prep = GNNDataPrep()
    x, edge_index, edge_type, rel2id, train_triples, val_triples, test_triples = data_prep.prepare_data()
    print(f"Node features shape: {x.shape}")
    print(f"Edge index shape: {edge_index.shape}")
    print(f"Edge type shape: {edge_type.shape}")
    print(f"Number of relations: {len(rel2id)}")
    print(f"Train triples: {len(train_triples)}, Val triples: {len(val_triples)}, Test triples: {len(test_triples)}")
    print("Data preparation complete.")
    subjects = edge_index[0][150:160]
    objects = edge_index[1][150:160]
    predicates = edge_type[150:160]

   