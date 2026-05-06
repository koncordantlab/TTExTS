import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import roc_auc_score
import pickle

class LinkPredictor:
    def __init__(self, model, graph):
        """
        Initialize the LinkPredictor with a trained embedding model.

        :param model: Trained Word2Vec model
        """
        self.model = model
        self.graph = graph
        self.book_nodes = self.get_book_nodes()


    def get_book_nodes(self):
        rdf_type = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
        book_class = "https://koncordantlab.com/TTEXTS/Text"

        book_nodes = set()

        # MultiDiGraph-safe iteration (doesn't miss parallel edges)
        # for s, o, k, data in self.graph.edges(keys=True, data=True):
        #     if data.get("relation") == rdf_type and o == book_class:
        #         book_nodes.add(s)

        for u, v, data in self.graph.edges(data=True):
            if data.get("relation") == rdf_type:
                if v == book_class:
                    book_nodes.add(u)
                elif u == book_class:
                    book_nodes.add(v)
        if 'http://www.w3.org/2002/07/owl#Class' in book_nodes:
            book_nodes.remove('http://www.w3.org/2002/07/owl#Class')
        
        with open("data/book_nodes.txt", "w") as f:
            for book in sorted(book_nodes):
                f.write(book + "\n")

        return list(book_nodes)

    def compute_score(self, head, tail):
        """
        Compute similarity score between two nodes.

        :param head: Head node
        :param tail: Tail node
        :return: Cosine similarity score
        """
        try:
            head_vec = self.model.wv[str(head)]
            tail_vec = self.model.wv[str(tail)]
            score = cosine_similarity([head_vec], [tail_vec])[0][0]
        except KeyError:
            # If a node is missing in embeddings
            score = 0
        return score

    def evaluate(self, positive_samples, negative_samples):
        """
        Evaluate the model using positive and negative samples.

        :param positive_samples: List of positive triples
        :param negative_samples: List of negative triples
        :return: AUC score
        """
        y_true = [1] * len(positive_samples) + [0] * len(negative_samples)
        y_scores = []

        for h, r, t in positive_samples:
            y_scores.append(self.compute_score(h, t))
        for h, r, t in negative_samples:
            y_scores.append(self.compute_score(h, t))

        auc_score = roc_auc_score(y_true, y_scores)
        return auc_score
    
    def get_similar_books(self, top_n=5):
        """
        Compute similarity between book nodes and retrieve the most similar books.

        :param book_nodes: List of book nodes
        :param top_n: Number of similar books to return
        :return: Dictionary of book nodes with their most similar books
        """
        similar_books = {}
        book_vectors = {
            str(book): self.model.wv[str(book)] for book in self.book_nodes if str(book) in self.model.wv
        }


        for book, vector in book_vectors.items():
            similarities = [
                (other_book, cosine_similarity([vector], [book_vectors[other_book]])[0][0])
                for other_book in book_vectors if other_book != book
            ]
            similar_books[book] = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_n]

        return similar_books
    
    @staticmethod
    def hit_at_k(ground_truth, predictions, k):
        hits = 0
        # print(predictions)
        for node, true_items in ground_truth.items():
            # Convert predictions to a set of node IDs
            predicted_items = {(p[0] if type(p) is not str else p) for p in predictions.get(node, [])[:k]}
            if any(item in true_items for item in predicted_items):
                hits += 1
            
        return hits / len(ground_truth)

    @staticmethod
    def mean_reciprocal_rank(ground_truth, predictions):
        mrr = 0
        for node, true_items in ground_truth.items():
            predicted_items = [(p[0] if type(p) is not str else p) for p in predictions.get(node, [])]
            for rank, item in enumerate(predicted_items, start=1):
                if item in true_items:
                    mrr += 1 / rank
                    break
        return mrr / len(ground_truth)

    @staticmethod
    def normalized_discounted_cumulative_gain(ground_truth, predictions, k):
        def dcg(relevances):
            return sum(rel / np.log2(idx + 2) for idx, rel in enumerate(relevances))

        ndcg = 0
        for node, true_items in ground_truth.items():
            predicted_items = [p[0] if type(p) is not str else p for p in predictions.get(node, [])[:k]]
            relevances = [1 if item in true_items else 0 for item in predicted_items]
            ideal_relevances = sorted(relevances, reverse=True)
            ndcg += dcg(relevances) / (dcg(ideal_relevances) or 1)
        return ndcg / len(ground_truth)
    


if __name__ == "__main__":
    with open('data/graphs/networkx_graph.gpickle', "rb") as f:
        G = pickle.load(f)

    link_predictor = LinkPredictor(model=None, graph=G)
    book_nodes = link_predictor.get_book_nodes()
    # print(book_nodes)
