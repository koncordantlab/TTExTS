import random

class NegativeSampler:
    def __init__(self, edges, all_nodes, random_state=42):
        """
        Initialize the NegativeSampler with edges and nodes.

        :param edges: List of triples (head, relation, tail)
        :param all_nodes: Set of all nodes/entities in the graph
        """
        self.edges = edges
        self.edges_set = set(edges)
        self.all_nodes = list(all_nodes)
        self.rng = random.Random(random_state)


    def generate_negative_samples(self, num_samples):
        """
        Generate negative samples by replacing head or tail entities.

        :param num_samples: Number of negative samples to generate
        :return: List of negative samples (triples)
        """
        negative_samples = set()
        while len(negative_samples) < num_samples:
            h, r, t = self.rng.choice(self.edges)

            if self.rng.random() < 0.5:
                h_neg = self.rng.choice(list(self.all_nodes))
                while (h_neg, r, t) in self.edges_set or h_neg == h:
                    h_neg = self.rng.choice(list(self.all_nodes))
                negative_samples.add((h_neg, r, t))
            else:
                t_neg = self.rng.choice(list(self.all_nodes))
                while (h, r, t_neg) in self.edges_set or t_neg == t:
                    t_neg = self.rng.choice(list(self.all_nodes))
                negative_samples.add((h, r, t_neg))

        return sorted(list(negative_samples))