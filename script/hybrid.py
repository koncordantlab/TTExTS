from link_predictor import LinkPredictor
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
import numpy as np
from sklearn.metrics import roc_auc_score
from data_prep import DataPrep


class Hybrid:
    def __init__(self, model1, model2, owl_file_path):
        self.model1 = model1
        self.model2 = model2
        self.owl_file_path = owl_file_path
        self.book_nodes = LinkPredictor(model1,self.owl_file_path).get_book_nodes()

    def get_hybrid_emb(self, node):  
        return np.concatenate((np.array(self.model1.wv[str(node)]), np.array(self.model2.wv[str(node)])))


    def get_similar_books(self, top_n):
        # linkPredictor_model1 = LinkPredictor(model=self.model1, owl_file=self.owl_file_path)
        # linkPredictor_model1 = LinkPredictor(model=self.model2, owl_file=self.owl_file_path)
        
        similar_books = {}
        book_vectors = {
            str(book): self.get_hybrid_emb(book) for book in self.book_nodes if str(book) in self.model1.wv
        }

        for book, vector in book_vectors.items():
            similarities = [
                (other_book, cosine_similarity([vector], [book_vectors[other_book]])[0][0])
                for other_book in book_vectors if other_book != book
            ]
            similar_books[book] = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_n]

        return similar_books
    
    def compute_score(self, head, tail):
        try:
            head_vec = self.get_hybrid_emb(head)
            tail_vec = self.get_hybrid_emb(tail)
            score = cosine_similarity([head_vec], [tail_vec])[0][0]
        except KeyError:
            # If a node is missing in embeddings
            score = 0
        return score
    
    def get_auc_score(self, positive_samples, negative_samples):
        y_true = [1] * len(positive_samples) + [0] * len(negative_samples)
        y_scores = []

        for h, r, t in positive_samples:
            y_scores.append(self.compute_score(h,t))
        for h, r, t in negative_samples:
            y_scores.append(self.compute_score(h,t))

        auc_score = roc_auc_score(y_true, y_scores)
        return auc_score

if __name__ == "__main__":
    model1 = Word2Vec.load('./data/deepwalk_30_30_128_20.model')
    model2 = Word2Vec.load('./data/biased_deepwalk_60_40_512_20.model')
    owl_file_path = "./data/output1.owl"
    hybrid = Hybrid(model1, model2, owl_file_path)

    prep = DataPrep(graph_file="./data/graph.gpickle")
    G, train_edges, val_edges, test_edges, all_nodes = prep.train_test_val_split(random_state=42)
    train_neg_samples, val_neg_samples, test_neg_samples = prep.negative_sampling(G, train_edges, val_edges, test_edges, all_nodes, random_state=42)

    print(hybrid.get_auc_score(test_edges, test_neg_samples))
