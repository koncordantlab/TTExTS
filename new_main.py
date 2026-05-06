"""
T-TExTS training pipeline.

Runs all experiments across (dataset_size x weight_config) combinations in
a single invocation. Key design goals:

  1. Reproducibility: seeded everywhere (Optuna sampler, NumPy, random,
     Word2Vec). Models re-run should produce identical embeddings.
  2. Persistence: best hyperparameters are saved as JSON alongside every
     saved model, so they can never be lost to a log overwrite again.
  3. Resumability: if a model file + its .params.json file both exist,
     that stage is skipped. Delete those files (or set FORCE_RETUNE=True)
     to re-tune from scratch.
  4. Fresh logs: every invocation writes to a new timestamped log file so
     no previous run is ever overwritten.

Outputs per run:
  data/models/<method>_hp_tuned_<size>[_<config>].model         trained Word2Vec
  data/models/<method>_hp_tuned_<size>[_<config>].params.json   best hyperparameters
  data/logs/experiments_<timestamp>.log                         full run log
  data/results/results_<timestamp>.json                         aggregated metrics
  data/results/results_<timestamp>.csv                          flat metrics for Excel
  data/recommendations/*.txt                                    top-K per anchor text
"""

import os
import sys
import json
import csv
import pickle
import random
import logging
from datetime import datetime

import numpy as np
import networkx as nx
import optuna
from tqdm import tqdm
from rdflib import Graph, Literal
from gensim.models import Word2Vec

from data_prep import DataPrep
from deepwalk_trainer import DeepwalkTrainer
from biased_random_walker import BiasedRandomWalker
from node2vec_trainer import Node2Vec
from link_predictor import LinkPredictor
from hyper_parameter_tuner import HyperParameterTuner
from hybrid import Hybrid
from utils.utils import setup_logging

sys.stderr = open(os.devnull, 'w')

# ==========================================================================
# CONFIGURATION
# ==========================================================================

SEED = 42
N_OPTUNA_TRIALS = 50

# Set to True to force re-tuning even if saved models exist.
# Alternatively, just delete the .model and .params.json files you want to
# redo and leave this False; the script will re-tune only the missing ones.
FORCE_RETUNE = False

DATASETS = [
    {"size": "98",  "ground_truth_size": "19"},
    {"size": "196", "ground_truth_size": "39"},
    {"size": "351", "ground_truth_size": "65"},
]

BASE_NS = "https://koncordantlab.com/TTEXTS/"

WEIGHT_CONFIGS = {
    # Default pedagogy-balanced weights. Genre, theme, subtheme are equally
    # emphasized; qualitative measures are weighted lower; anything else = 1.
    "default": {
        f"{BASE_NS}has_genre": 3,
        f"{BASE_NS}has_theme": 3,
        f"{BASE_NS}has_subtheme": 3,
        f"{BASE_NS}has_levels_of_meaning": 2,
        f"{BASE_NS}has_text_structure": 2,
        f"{BASE_NS}has_language_conventionality_and_clarity": 2,
        f"{BASE_NS}has_knowledge_demands": 2,
        "Others": 1,
    },
    # Genre-emphasized. Only has_genre is raised to 4; everything else same.
    # Used to measure sensitivity of Biased RW and Hybrid to genre weight.
    "genre_emphasized": {
        f"{BASE_NS}has_genre": 4,
        f"{BASE_NS}has_theme": 3,
        f"{BASE_NS}has_subtheme": 3,
        f"{BASE_NS}has_levels_of_meaning": 2,
        f"{BASE_NS}has_text_structure": 2,
        f"{BASE_NS}has_language_conventionality_and_clarity": 2,
        f"{BASE_NS}has_knowledge_demands": 2,
        "Others": 1,
    },
}


# ==========================================================================
# SETUP
# ==========================================================================

# Global seeds. Any downstream component that uses the standard `random` or
# `numpy.random` modules will pick these up. Trainer classes must also pass
# workers=1 and seed=SEED into their Word2Vec call (see notes at bottom).
random.seed(SEED)
np.random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)

for directory in [
    "data/logs", "data/models", "data/graphs",
    "data/recommendations", "data/results",
]:
    os.makedirs(directory, exist_ok=True)

# Timestamped log filename so reruns never overwrite previous logs.
RUN_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE = f"data/logs/experiments_{RUN_TIMESTAMP}.log"
logger = setup_logging(LOG_FILE)

logging.getLogger("rdflib").setLevel(logging.ERROR)
logging.getLogger("gensim").setLevel(logging.ERROR)
# Use INFO so each Optuna trial is logged as it completes. Change to WARNING
# if you find the output too chatty once you're past the debugging phase.
logging.getLogger("optuna").setLevel(logging.INFO)
# Silence the C-extension warnings from gensim without hiding tqdm output.
import warnings
warnings.filterwarnings("ignore")

logger.info(f"Run timestamp     : {RUN_TIMESTAMP}")
logger.info(f"Seed              : {SEED}")
logger.info(f"Optuna n_trials   : {N_OPTUNA_TRIALS}")
logger.info(f"Force retune      : {FORCE_RETUNE}")
logger.info(f"Datasets          : {[d['size'] for d in DATASETS]}")
logger.info(f"Weight configs    : {list(WEIGHT_CONFIGS.keys())}")


# ==========================================================================
# HELPERS
# ==========================================================================

def save_params(params: dict, path: str) -> None:
    """Persist hyperparameters as JSON alongside the model file."""
    with open(path, "w") as f:
        json.dump(params, f, indent=2)
    logger.info(f"Saved hyperparameters -> {path}")


def load_params(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def artifacts_exist(model_path: str, params_path: str) -> bool:
    """Both model and params JSON must exist to consider the stage done."""
    return os.path.exists(model_path) and os.path.exists(params_path)


def make_optuna_study() -> optuna.Study:
    """Create a new Optuna study with a seeded TPE sampler.

    Passing this into HyperParameterTuner guarantees the search trajectory
    is identical across invocations.

    The returned study has its `optimize` method monkey-patched so that
    every call automatically gets `show_progress_bar=True`. That way you
    see a tqdm progress bar during tuning without needing to modify your
    HyperParameterTuner class at all.
    """
    study = optuna.create_study(
        direction="maximize",
        sampler=optuna.samplers.TPESampler(seed=SEED),
    )

    # Wrap study.optimize so every invocation shows a tqdm progress bar.
    _original_optimize = study.optimize

    def _optimize_with_progress(*args, **kwargs):
        kwargs.setdefault("show_progress_bar", True)
        return _original_optimize(*args, **kwargs)

    study.optimize = _optimize_with_progress
    return study


def write_recommendations(path: str, recommendations: dict) -> None:
    """Write top-K recommendations to disk if not already present."""
    if os.path.exists(path):
        return
    with open(path, "w") as f:
        for book, results in recommendations.items():
            f.write(f"The top recommendations for {book} are:\n")
            for result in results:
                f.write(f"{result[0]}\n")
            f.write("\n")


def compute_all_metrics(link_predictor, similar_books, ground_truth,
                        test_edges, test_neg_samples) -> dict:
    """Compute the six metrics reported in the paper, plus AUC."""
    return {
        "AUC":     link_predictor.evaluate(test_edges, test_neg_samples),
        "Hit@1":   link_predictor.hit_at_k(ground_truth, similar_books, k=1),
        "Hit@3":   link_predictor.hit_at_k(ground_truth, similar_books, k=3),
        "Hit@5":   link_predictor.hit_at_k(ground_truth, similar_books, k=5),
        "Hit@10":  link_predictor.hit_at_k(ground_truth, similar_books, k=10),
        "MRR":     link_predictor.mean_reciprocal_rank(ground_truth, similar_books),
        "NDCG@10": link_predictor.normalized_discounted_cumulative_gain(
                       ground_truth, similar_books, k=10),
    }


def format_metrics(metrics: dict) -> str:
    return ", ".join(f"{k}={v:.4f}" for k, v in metrics.items())


def build_networkx_graph(owl_file_path: str, nx_graph_path: str) -> None:
    """Parse the OWL file and cache it as a NetworkX MultiGraph pickle."""
    rdf_graph = Graph()
    rdf_graph.parse(owl_file_path, format="xml")

    nx_graph = nx.MultiGraph()
    for s, p, o in rdf_graph:
        if not isinstance(o, Literal):
            nx_graph.add_edge(str(s), str(o), relation=str(p))

    with open(nx_graph_path, "wb") as f:
        pickle.dump(nx_graph, f)

    logger.info(
        f"Built NetworkX graph: {len(rdf_graph)} RDF triples, "
        f"{nx_graph.number_of_edges()} non-literal edges, "
        f"{len(rdf_graph) - nx_graph.number_of_edges()} literals discarded"
    )


# ==========================================================================
# MAIN PIPELINE
# ==========================================================================

# Count the total number of tuning-or-training stages so we can display
# an outer "experiment X of N" counter alongside Optuna's inner tqdm bar.
# Total = (DeepWalk + Node2Vec) * n_datasets + BiasedRW * n_datasets * n_configs
TOTAL_STAGES = (2 * len(DATASETS)) + (len(DATASETS) * len(WEIGHT_CONFIGS))
current_stage = [0]  # list so inner closures can mutate it

def stage_banner(label: str) -> None:
    """Print a visible banner before each tuning stage so progress is clear."""
    current_stage[0] += 1
    msg = f">>> STAGE {current_stage[0]:2d}/{TOTAL_STAGES}: {label}"
    logger.info(msg)
    # Also print directly so it shows up above Optuna's tqdm bar, not just
    # in the log file. tqdm writes to stderr; a plain print goes to stdout.
    print(msg, flush=True)

all_results = {}  # keyed by "{size}_{weight_config}"

for dataset in tqdm(DATASETS, desc="Datasets", position=0):
    dataset_size = dataset["size"]
    gt_size = dataset["ground_truth_size"]

    logger.info("=" * 78)
    logger.info(f"DATASET: {dataset_size} texts (ground truth size: {gt_size})")
    logger.info("=" * 78)

    owl_path = f"data/owls/output_{dataset_size}.owl"
    nx_path = f"data/graphs/networkx_graph_{dataset_size}.gpickle"
    dw_graph_path = f"data/graphs/deepwalk_graph_{dataset_size}.gpickle"

    # --- Build or load the NetworkX graph ------------------------------------
    if not os.path.exists(nx_path):
        build_networkx_graph(owl_path, nx_path)
    else:
        logger.info(f"Using cached NetworkX graph: {nx_path}")

    # --- Seeded split + negative sampling ------------------------------------
    prep = DataPrep(graph_file=nx_path)
    G, train_edges, val_edges, test_edges, all_nodes = prep.train_test_val_split(
        random_state=SEED
    )
    train_neg, val_neg, test_neg = prep.negative_sampling(
        train_edges, val_edges, test_edges, all_nodes, random_state=SEED
    )

    prep.save_deepwalk_graph(G, train_edges, dw_graph_path)
    with open(dw_graph_path, "rb") as f:
        deepwalk_graph = pickle.load(f)

    ground_truth = prep.get_ground_truth(f"data/ground_truth_{gt_size}.csv")

    # =========================================================================
    # DeepWalk (weight-independent; trained once per dataset)
    # =========================================================================
    dw_model_path = f"data/models/deepwalk_hp_tuned_{dataset_size}.model"
    dw_params_path = f"data/models/deepwalk_hp_tuned_{dataset_size}.params.json"

    if artifacts_exist(dw_model_path, dw_params_path) and not FORCE_RETUNE:
        logger.info(f"[DeepWalk:{dataset_size}] loading cached model and params")
        dw_model = Word2Vec.load(dw_model_path)
        dw_params = load_params(dw_params_path)
    else:
        stage_banner(f"DeepWalk tuning for {dataset_size} books")
        tuner = HyperParameterTuner(
            G,
            test_edges=val_edges,
            test_neg_samples=val_neg,
            study=make_optuna_study(),
        )
        dw_params = tuner.tune_hyperparameters(
            n_trials=N_OPTUNA_TRIALS, method="deepwalk"
        )
        logger.info(f"[DeepWalk:{dataset_size}] best params: {dw_params}")

        dw_trainer = DeepwalkTrainer(
            G,
            walk_length=dw_params["walk_length"],
            num_walks=dw_params["num_walks"],
            dimensions=dw_params["dimensions"],
            window_size=dw_params["window_size"],
            workers=1,
            seed=SEED,
        )
        dw_model = dw_trainer.train_embeddings()
        dw_model.save(dw_model_path)
        save_params(dw_params, dw_params_path)

    dw_lp = LinkPredictor(dw_model, G)
    dw_similar = dw_lp.get_similar_books(top_n=15)
    dw_metrics = compute_all_metrics(
        dw_lp, dw_similar, ground_truth, test_edges, test_neg
    )
    logger.info(f"[DeepWalk:{dataset_size}] {format_metrics(dw_metrics)}")
    write_recommendations(
        f"data/recommendations/final_recommendation_deepwalk_{dataset_size}.txt",
        dw_similar,
    )

    # =========================================================================
    # Node2Vec (weight-independent; trained once per dataset)
    # =========================================================================
    n2v_model_path = f"data/models/node2vec_hp_tuned_{dataset_size}.model"
    n2v_params_path = f"data/models/node2vec_hp_tuned_{dataset_size}.params.json"

    if artifacts_exist(n2v_model_path, n2v_params_path) and not FORCE_RETUNE:
        logger.info(f"[Node2Vec:{dataset_size}] loading cached model and params")
        n2v_model = Word2Vec.load(n2v_model_path)
        n2v_params = load_params(n2v_params_path)
    else:
        stage_banner(f"Node2Vec tuning for {dataset_size} books")
        tuner = HyperParameterTuner(
            G,
            test_edges=val_edges,
            test_neg_samples=val_neg,
            study=make_optuna_study(),
        )
        n2v_params = tuner.tune_hyperparameters(
            n_trials=N_OPTUNA_TRIALS, method="node2vec"
        )
        logger.info(f"[Node2Vec:{dataset_size}] best params: {n2v_params}")

        n2v_trainer = Node2Vec(
            G=G,
            walk_length=n2v_params["walk_length"],
            num_walks=n2v_params["num_walks"],
            dimensions=n2v_params["dimensions"],
            window_size=n2v_params["window_size"],
            p=n2v_params.get("node2vec_p", 1.0),
            q=n2v_params.get("node2vec_q", 1.0),
            workers=1,
            seed=SEED,
        )
        walks = n2v_trainer.simulate_walks()
        n2v_model = n2v_trainer.train_embeddings(walks=walks)
        n2v_model.save(n2v_model_path)
        save_params(n2v_params, n2v_params_path)

    n2v_lp = LinkPredictor(n2v_model, G)
    n2v_similar = n2v_lp.get_similar_books(top_n=15)
    n2v_metrics = compute_all_metrics(
        n2v_lp, n2v_similar, ground_truth, test_edges, test_neg
    )
    logger.info(f"[Node2Vec:{dataset_size}] {format_metrics(n2v_metrics)}")
    write_recommendations(
        f"data/recommendations/final_recommendation_node2vec_{dataset_size}.txt",
        n2v_similar,
    )

    # =========================================================================
    # Biased RW + Hybrid (one per weight config)
    # =========================================================================
    for config_name, weights in tqdm(
        WEIGHT_CONFIGS.items(),
        desc=f"Configs (n={dataset_size})",
        total=len(WEIGHT_CONFIGS),
        position=1,
        leave=False,
    ):
        logger.info("-" * 78)
        logger.info(f"WEIGHT CONFIG: {config_name}  |  dataset: {dataset_size}")
        logger.info("-" * 78)

        bias_model_path = (
            f"data/models/biased_rw_hp_tuned_{dataset_size}_{config_name}.model"
        )
        bias_params_path = (
            f"data/models/biased_rw_hp_tuned_{dataset_size}_{config_name}.params.json"
        )

        if artifacts_exist(bias_model_path, bias_params_path) and not FORCE_RETUNE:
            logger.info(
                f"[Biased RW:{dataset_size}:{config_name}] loading cached model"
            )
            bias_model = Word2Vec.load(bias_model_path)
            bias_params = load_params(bias_params_path)
        else:
            stage_banner(
                f"Biased RW tuning for {dataset_size} books ({config_name} weights)"
            )
            bias_tuner = HyperParameterTuner(
                deepwalk_graph,
                test_edges=val_edges,
                test_neg_samples=val_neg,
                relation_weights=weights,
                study=make_optuna_study(),
            )
            bias_params = bias_tuner.tune_hyperparameters(
                n_trials=N_OPTUNA_TRIALS, method="biased_random_walk"
            )
            logger.info(
                f"[Biased RW:{dataset_size}:{config_name}] "
                f"best params: {bias_params}"
            )

            bias_trainer = BiasedRandomWalker(
                relation_weights=weights,
                graph=deepwalk_graph,
                walk_length=bias_params["walk_length"],
                num_walks=bias_params["num_walks"],
                dimensions=bias_params["dimensions"],
                window_size=bias_params["window_size"],
                workers=1,
                seed=SEED,
            )
            bias_model = bias_trainer.train_embeddings()
            bias_model.save(bias_model_path)
            save_params(bias_params, bias_params_path)

        bias_lp = LinkPredictor(bias_model, G)
        bias_similar = bias_lp.get_similar_books(top_n=15)
        bias_metrics = compute_all_metrics(
            bias_lp, bias_similar, ground_truth, test_edges, test_neg
        )
        logger.info(
            f"[Biased RW:{dataset_size}:{config_name}] "
            f"{format_metrics(bias_metrics)}"
        )
        write_recommendations(
            f"data/recommendations/final_recommendation_biased_rw_"
            f"{dataset_size}_{config_name}.txt",
            bias_similar,
        )

        # ---- Hybrid: DeepWalk embeddings + this config's Biased RW ----------
        hybrid = Hybrid(dw_model, bias_model, G)
        hyb_similar = hybrid.get_similar_books(top_n=15)
        hyb_metrics = {
            "AUC":     hybrid.get_auc_score(test_edges, test_neg),
            "Hit@1":   LinkPredictor.hit_at_k(ground_truth, hyb_similar, k=1),
            "Hit@3":   LinkPredictor.hit_at_k(ground_truth, hyb_similar, k=3),
            "Hit@5":   LinkPredictor.hit_at_k(ground_truth, hyb_similar, k=5),
            "Hit@10":  LinkPredictor.hit_at_k(ground_truth, hyb_similar, k=10),
            "MRR":     LinkPredictor.mean_reciprocal_rank(ground_truth, hyb_similar),
            "NDCG@10": LinkPredictor.normalized_discounted_cumulative_gain(
                           ground_truth, hyb_similar, k=10),
        }
        logger.info(
            f"[Hybrid:{dataset_size}:{config_name}] "
            f"{format_metrics(hyb_metrics)}"
        )
        write_recommendations(
            f"data/recommendations/final_recommendation_hybrid_"
            f"{dataset_size}_{config_name}.txt",
            hyb_similar,
        )

        # ---- Store results ---------------------------------------------------
        key = f"{dataset_size}_{config_name}"
        all_results[key] = {
            "dataset_size":  dataset_size,
            "weight_config": config_name,
            "DeepWalk":      dw_metrics,
            "Biased_RW":     bias_metrics,
            "Hybrid":        hyb_metrics,
            "Node2Vec":      n2v_metrics,
            "hyperparameters": {
                "DeepWalk":  dw_params,
                "Biased_RW": bias_params,
                "Node2Vec":  n2v_params,
            },
        }


# ==========================================================================
# AGGREGATE AND WRITE RESULTS
# ==========================================================================

results_json = f"data/results/results_{RUN_TIMESTAMP}.json"
with open(results_json, "w") as f:
    json.dump(all_results, f, indent=2)
logger.info(f"Wrote aggregated results JSON -> {results_json}")

# Flat CSV for easy pasting into your Excel workbook.
results_csv = f"data/results/results_{RUN_TIMESTAMP}.csv"
with open(results_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "dataset_size", "weight_config", "model",
        "AUC", "Hit@1", "Hit@3", "Hit@5", "Hit@10", "MRR", "NDCG@10",
    ])
    for res in all_results.values():
        for model_name in ["DeepWalk", "Biased_RW", "Hybrid", "Node2Vec"]:
            m = res[model_name]
            writer.writerow([
                res["dataset_size"], res["weight_config"], model_name,
                f"{m['AUC']:.4f}",    f"{m['Hit@1']:.4f}",  f"{m['Hit@3']:.4f}",
                f"{m['Hit@5']:.4f}",  f"{m['Hit@10']:.4f}",
                f"{m['MRR']:.4f}",    f"{m['NDCG@10']:.4f}",
            ])
logger.info(f"Wrote aggregated results CSV  -> {results_csv}")

logger.info("=" * 78)
logger.info("ALL EXPERIMENTS COMPLETE")
logger.info(f"Log file: {LOG_FILE}")
logger.info("=" * 78)

