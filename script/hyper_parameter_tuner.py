import optuna
from deepwalk_trainer import DeepwalkTrainer
from link_predictor import LinkPredictor
import networkx as nx

class HyperParameterTuner:
    def __init__(self, graph, test_edges, test_neg_samples, owl_file):
        """
        Initialize the HyperParameterTuner.

        :param graph: NetworkX graph
        :param test_edges: List of test edges
        :param test_neg_samples: List of negative test samples
        :param book_nodes: List of book nodes
        """
        self.graph = graph
        self.test_edges = test_edges
        self.test_neg_samples = test_neg_samples
        self.owl_file = owl_file

        # Define predefined hyperparameter values to sample from
        self.hyperparameter_options = {
            "walk_length": [15, 20, 25, 30, 40, 60],
            "num_walks": [15, 20, 25, 30, 40],
            "dimensions": [128, 256, 512],
            "window_size": [5, 10, 15, 20]
        }

    def sample_hyperparameter(self, trial, param_name):
        """Select a hyperparameter value from the predefined list"""
        return trial.suggest_categorical(param_name, self.hyperparameter_options[param_name])

    def objective(self, trial):
        """Objective function for Optuna"""
        walk_length = self.sample_hyperparameter(trial, "walk_length")
        num_walks = self.sample_hyperparameter(trial, "num_walks")
        dimensions = self.sample_hyperparameter(trial, "dimensions")
        window_size = self.sample_hyperparameter(trial, "window_size")

        deepwalk_trainer = DeepwalkTrainer(
            self.graph,
            walk_length=walk_length,
            num_walks=num_walks,
            dimensions=dimensions,
            window_size=window_size,
            workers=4
        )
        model = deepwalk_trainer.train_embeddings()
        link_predictor = LinkPredictor(model, self.owl_file)
        auc_score = link_predictor.evaluate(self.test_edges, self.test_neg_samples)
        
        return auc_score

    def tune_hyperparameters(self, n_trials=20):
        """
        Run Optuna hyperparameter tuning.

        :param n_trials: Number of trials to run
        :return: Best set of hyperparameters
        """
        study = optuna.create_study(direction="maximize")
        study.optimize(self.objective, n_trials=n_trials)

        print(f"\n✅ Best Hyperparameters: {study.best_params}")
        return study.best_params



if __name__ == "__main__":
    from data_prep import DataPrep
    from link_predictor import LinkPredictor

    # Load the graph
    G = nx.read_gpickle("./data/graph.gpickle")

    prep = DataPrep(graph_file="./data/graph.gpickle")
    G, train_edges, val_edges, test_edges, all_nodes = prep.train_test_val_split()
    train_neg_samples, val_neg_samples, test_neg_samples = prep.negative_sampling(G, train_edges, val_edges, test_edges, all_nodes) 

    # Perform hyperparameter tuning
    tuner = HyperParameterTuner(G, test_edges, test_neg_samples, owl_file="./data/output.owl")
    best_params = tuner.tune_hyperparameters(n_trials=50)

    print(best_params)