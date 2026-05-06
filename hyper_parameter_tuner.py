import optuna
import networkx as nx
from link_predictor import LinkPredictor

from deepwalk_trainer import DeepwalkTrainer
from biased_random_walker import BiasedRandomWalker
from node2vec_trainer import Node2Vec

class HyperParameterTuner:
    def __init__(self, graph, test_edges, test_neg_samples, relation_weights=None, study=None):
        self.graph = graph
        self.test_edges = test_edges
        self.test_neg_samples = test_neg_samples
        self.relation_weights = relation_weights  # Store for biased walks
        self.study = study if study is not None else optuna.create_study(direction="maximize", sampler=optuna.samplers.TPESampler(seed=42))

        self.hyperparameter_options = {
            "walk_length": [20, 30, 40, 60, 80, 100],
            "num_walks": [10, 20, 25, 30, 40, 50],
            "dimensions": [128, 256, 512, 1024],
            "window_size": [10, 15, 20, 25, 30],
            "node2vec_p": [0.25, 0.5, 1.0, 2.0, 4.0],
            "node2vec_q": [0.25, 0.5, 1.0, 2.0, 4.0],
        }

        self.method_map = {
            "deepwalk": DeepwalkTrainer,
            "biased_random_walk": BiasedRandomWalker,
            "node2vec": Node2Vec
        }

    def _sample_params(self, trial, method):
        """Samples standard and method-specific hyperparameters."""
        params = {
            "walk_length": trial.suggest_categorical("walk_length", self.hyperparameter_options["walk_length"]),
            "num_walks": trial.suggest_categorical("num_walks", self.hyperparameter_options["num_walks"]),
            "dimensions": trial.suggest_categorical("dimensions", self.hyperparameter_options["dimensions"]),
            "window_size": trial.suggest_categorical("window_size", self.hyperparameter_options["window_size"]),
            "workers": 4
        }

        if method == "node2vec":
            params["p"] = trial.suggest_categorical("node2vec_p", self.hyperparameter_options["node2vec_p"])
            params["q"] = trial.suggest_categorical("node2vec_q", self.hyperparameter_options["node2vec_q"])
        
        elif method == "biased_random_walk":
            params["relation_weights"] = self.relation_weights

        return params

    def _objective(self, trial, method):
        """Universal objective function for all methods."""
        TrainerClass = self.method_map[method]
        params = self._sample_params(trial, method)

        # Initialize and train
        trainer = TrainerClass(self.graph, **params)
        model = trainer.train_embeddings()
        
        # Evaluate
        link_predictor = LinkPredictor(model, self.graph)
        return link_predictor.evaluate(self.test_edges, self.test_neg_samples)

    def tune_hyperparameters(self, n_trials=20, method="deepwalk"):
        """Main entry point for tuning."""
        if method not in self.method_map:
            raise ValueError(f"Unknown method: {method}. Choose from {list(self.method_map.keys())}")

        # Use a lambda to pass the 'method' argument to the objective
        self.study.optimize(lambda trial: self._objective(trial, method), n_trials=n_trials)

        print(f"\n✅ Best Hyperparameters for {method}: {self.study.best_params}")
        return self.study.best_params