# from owl2graph import OWL2Graph 
from data_prep import DataPrep
import pickle
from deepwalk_trainer import DeepwalkTrainer
from link_predictor import LinkPredictor
from hyper_parameter_tuner import HyperParameterTuner
from rdflib import Graph
from gensim.models import Word2Vec
import random
import numpy as np
from hybrid import Hybrid
from node2vec_trainer import Node2Vec

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

owl_file_path = "./data/output1.owl"
# converter = OWL2Graph(owl_file_path)
# converter.run_conversion()

prep = DataPrep(graph_file="./data/graph.gpickle")
G, train_edges, val_edges, test_edges, all_nodes = prep.train_test_val_split(random_state=SEED)
train_neg_samples, val_neg_samples, test_neg_samples = prep.negative_sampling(G, train_edges, val_edges, test_edges, all_nodes, random_state=SEED)
# prep.save_deepwalk_graph(G, train_edges, "./data/deepwalk_graph.gpickle")

with open('./data/deepwalk_graph.gpickle', "rb") as f:
    deepwalk_graph = pickle.load(f)

# trainer = DeepwalkTrainer(deepwalk_graph)
# model = trainer.train_embeddings()
# model.save('./data/deepwalk_before_hp.model')

model = Word2Vec.load('./data/deepwalk_before_hp.model')
link_predictor = LinkPredictor(model, owl_file_path)
auc_score = link_predictor.evaluate(test_edges, test_neg_samples)
print(f"\nAUC Score before hyper-parameter tuning: {auc_score:.4f}")

# # g = Graph()
# # g.parse(owl_file_path, format='xml')
# # query = """
# # PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# # SELECT ?book
# # WHERE {
# #     ?book rdfs:subClassOf <https://koncordantlab.com/TTEXTS/Book> .
# # }
# # """
# # results = g.query(query)

# # book_nodes = [str(row.book) for row in results]

# # Perform hyperparameter tuning with Optuna
# tuner = HyperParameterTuner(G, test_edges=val_edges, test_neg_samples=val_neg_samples, owl_file=owl_file_path)
# best_params = tuner.tune_hyperparameters(n_trials=50)

# deepwalk_trainer = DeepwalkTrainer(
#         G,
#         walk_length=best_params['walk_length'],
#         num_walks=best_params['num_walks'],
#         dimensions=best_params['dimensions'],
#         window_size=best_params['window_size'],
#         workers=4
#     )
# model = deepwalk_trainer.train_embeddings()
# model.save('./data/deepwalk_hp_tuned.model')

# deepwalk_trainer = DeepwalkTrainer(
#         G,
#         walk_length=60,
#         num_walks=25,
#         dimensions=256,
#         window_size=20,
#         workers=4
#     )
# model = deepwalk_trainer.train_embeddings()
# model.save('./data/deepwalk_60_25_256_20_2.model')



# # model_hp_tuned = Word2Vec.load('./data/deepwalk_hp_tuned.model')
# model_hp_tuned = Word2Vec.load('./data/deepwalk_30_30_128_20.model')
model_hp_tuned = Word2Vec.load('./data/deepwalk_60_25_256_20_2.model')
link_predictor_hp_tuned = LinkPredictor(model_hp_tuned, owl_file_path)
final_auc = link_predictor_hp_tuned.evaluate(test_edges, test_neg_samples)
print(f"\nFinal AUC Score with deepwalk: {final_auc:.4f}")

similar_books_hp_tuned = link_predictor_hp_tuned.get_similar_books(top_n=15)

ground_truth = prep.get_ground_truth("./data/ground_truth.csv")

hit_at_10 = link_predictor_hp_tuned.hit_at_k(ground_truth, similar_books_hp_tuned, k=10)
hit_at_5 = link_predictor_hp_tuned.hit_at_k(ground_truth, similar_books_hp_tuned, k=5)
hit_at_3 = link_predictor_hp_tuned.hit_at_k(ground_truth, similar_books_hp_tuned, k=3)
hit_at_1 = link_predictor_hp_tuned.hit_at_k(ground_truth, similar_books_hp_tuned, k=1)
mrr = link_predictor_hp_tuned.mean_reciprocal_rank(ground_truth, similar_books_hp_tuned)
ndcg = link_predictor_hp_tuned.normalized_discounted_cumulative_gain(ground_truth, similar_books_hp_tuned, k=10)

print(f"Hit@10: {hit_at_10:.4f}")
print(f"Hit@5: {hit_at_5:.4f}")
print(f"Hit@3: {hit_at_3:.4f}")
print(f"Hit@1: {hit_at_1:.4f}")
print(f"MRR: {mrr:.4f}")
print(f"NDCG@10: {ndcg:.4f}")

with open('data/recommendations/deepwalk.txt', 'w') as f:
    for book in similar_books_hp_tuned.keys():
        f.write(f'The top 10 recommendations for {str(book)[38:]} are:\n')
        for result in similar_books_hp_tuned[book]:
            f.write(f'{str(result[0])[38:]}\n')
        f.write('\n')


# Test BiasedRandomWalker
import networkx as nx
from biased_random_walker import BiasedRandomWalker

# Define relation weights
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

# # Perform hyperparameter tuning with Optuna
# biased_tuner = HyperParameterTuner(deepwalk_graph, test_edges=val_edges, test_neg_samples=val_neg_samples, owl_file=owl_file_path)
# biased_best_params = biased_tuner.tune_hyperparameters(n_trials=50)

# biased_deepwalk_trainer = BiasedRandomWalker(
#         relation_weights=relation_weights,
#         graph=deepwalk_graph,
#         walk_length=biased_best_params['walk_length'],
#         num_walks=biased_best_params['num_walks'],
#         dimensions=biased_best_params['dimensions'],
#         window_size=biased_best_params['window_size'],
#         workers=4
#     )
# biased_model = biased_deepwalk_trainer.train_embeddings()
# biased_model.save('./data/biased_deepwalk_hp_tuned.model')

# biased_deepwalk_trainer = BiasedRandomWalker(
#         relation_weights=relation_weights,
#         graph=deepwalk_graph,
#         walk_length=60,
#         num_walks=40,
#         dimensions=512,
#         window_size=20,
#         workers=4
#     )
# biased_model = biased_deepwalk_trainer.train_embeddings()
# biased_model.save('./data/biased_deepwalk_60_40_512_20_2.model')

# # # biased_model = Word2Vec.load('./data/biased_deepwalk_hp_tuned.model')
# biased_model = Word2Vec.load('./data/biased_deepwalk_60_40_512_20.model')
biased_model = Word2Vec.load('./data/biased_deepwalk_60_40_512_20_2.model')
biased_link_predictor = LinkPredictor(biased_model, owl_file_path)
final_auc = biased_link_predictor.evaluate(test_edges, test_neg_samples)
print(f"\nFinal AUC Score of model with biased random walk: {final_auc:.4f}")

similar_books_biased = biased_link_predictor.get_similar_books(top_n=15)

ground_truth = prep.get_ground_truth("./data/ground_truth.csv")

hit_at_10_biased = biased_link_predictor.hit_at_k(ground_truth, similar_books_biased, k=10)
hit_at_5_biased = biased_link_predictor.hit_at_k(ground_truth, similar_books_biased, k=5)
hit_at_3_biased = biased_link_predictor.hit_at_k(ground_truth, similar_books_biased, k=3)
hit_at_1_biased = biased_link_predictor.hit_at_k(ground_truth, similar_books_biased, k=1)
mrr_biased = biased_link_predictor.mean_reciprocal_rank(ground_truth, similar_books_biased)
ndcg_biased = biased_link_predictor.normalized_discounted_cumulative_gain(ground_truth, similar_books_biased, k=10)

print(f"Hit@10: {hit_at_10_biased:.4f}")
print(f"Hit@5: {hit_at_5_biased:.4f}")
print(f"Hit@3: {hit_at_3_biased:.4f}")
print(f"Hit@1: {hit_at_1_biased:.4f}")
print(f"MRR: {mrr_biased:.4f}")
print(f"NDCG@10: {ndcg_biased:.4f}")

with open('data/recommendations/biased_random_walk.txt', 'w') as f:
    for book in similar_books_biased.keys():
        f.write(f'The top 10 recommendations for {str(book)[38:]} are:\n')
        for result in similar_books_biased[book]:
            f.write(f'{str(result[0])[38:]}\n')
        f.write('\n')

hybrid = Hybrid(model_hp_tuned, biased_model, owl_file_path)

similar_books_hybrid = hybrid.get_similar_books(top_n=15)

hit_at_10_hybrid = LinkPredictor.hit_at_k(ground_truth, similar_books_hybrid, k=10)
hit_at_5_hybrid = LinkPredictor.hit_at_k(ground_truth, similar_books_hybrid, k=5)
hit_at_3_hybrid = LinkPredictor.hit_at_k(ground_truth, similar_books_hybrid, k=3)
hit_at_1_hybrid = LinkPredictor.hit_at_k(ground_truth, similar_books_hybrid, k=1)
mrr_hybrid = LinkPredictor.mean_reciprocal_rank(ground_truth, similar_books_hybrid)
ndcg_hybrid = LinkPredictor.normalized_discounted_cumulative_gain(ground_truth, similar_books_hybrid, k=10)

print(f"\nFinal AUC Score of hybrid model: {hybrid.get_auc_score(test_edges, test_neg_samples):.4f}")
print(f"Results of the hybrid model: ")
print(f"Hit@10: {hit_at_10_hybrid:.4f}")
print(f"Hit@5: {hit_at_5_hybrid:.4f}")
print(f"Hit@3: {hit_at_3_hybrid:.4f}")
print(f"Hit@1: {hit_at_1_hybrid:.4f}")
print(f"MRR: {mrr_hybrid:.4f}")
print(f"NDCG@10: {ndcg_hybrid:.4f}")

with open('data/recommendations/hybrid.txt', 'w') as f:
    for book in similar_books_hybrid.keys():
        f.write(f'The top 10 recommendations for {str(book)[38:]} are:\n')
        for result in similar_books_hybrid[book]:
            f.write(f'{str(result[0])[38:]}\n')
        f.write('\n')


# node2vec_tuner = HyperParameterTuner(deepwalk_graph, test_edges=val_edges, test_neg_samples=val_neg_samples, owl_file=owl_file_path)
# best_params_node2vec = node2vec_tuner.tune_hyperparameters_node2vec(n_trials=50)
# node2vec_trainer = Node2Vec(
#         G=deepwalk_graph,
#         dimensions=best_params_node2vec['dimensions'],
#         walk_length=best_params_node2vec['walk_length'],
#         num_walks=best_params_node2vec['num_walks'],
#         window_size=best_params_node2vec['window_size'],
#         p=best_params_node2vec['p'],
#         q=best_params_node2vec['q'],
#         workers=4
#     )

# model_node2vec = node2vec_trainer.train_embeddings()
# model_node2vec.save('./data/node2vec_hp_tuned.model')

model_node2vec = Word2Vec.load('./data/node2vec_hp_tuned.model')
link_predictor_node2vec = LinkPredictor(model_node2vec, owl_file_path)
final_auc_node2vec = link_predictor_node2vec.evaluate(test_edges, test_neg_samples)
print(f"\nFinal AUC Score with Node2Vec: {final_auc_node2vec:.4f}")

similar_books_node2vec = link_predictor_node2vec.get_similar_books(top_n=15)
ground_truth = prep.get_ground_truth("./data/ground_truth.csv")
hit_at_10_node2vec = link_predictor_node2vec.hit_at_k(ground_truth, similar_books_node2vec, k=10)
hit_at_5_node2vec = link_predictor_node2vec.hit_at_k(ground_truth, similar_books_node2vec, k=5)
hit_at_3_node2vec = link_predictor_node2vec.hit_at_k(ground_truth, similar_books_node2vec, k=3)
hit_at_1_node2vec = link_predictor_node2vec.hit_at_k(ground_truth, similar_books_node2vec, k=1)
mrr_node2vec = link_predictor_node2vec.mean_reciprocal_rank(ground_truth, similar_books_node2vec)
ndcg_node2vec = link_predictor_node2vec.normalized_discounted_cumulative_gain(ground_truth, similar_books_node2vec, k=10)

print(f"Hit@10: {hit_at_10_node2vec:.4f}")
print(f"Hit@5: {hit_at_5_node2vec:.4f}")
print(f"Hit@3: {hit_at_3_node2vec:.4f}")
print(f"Hit@1: {hit_at_1_node2vec:.4f}")
print(f"MRR: {mrr_node2vec:.4f}")
print(f"NDCG@10: {ndcg_node2vec:.4f}")

with open('data/recommendations/node2vec.txt', 'w') as f:
    for book in similar_books_node2vec.keys():
        f.write(f'The top 10 recommendations for {str(book)[38:]} are:\n')
        for result in similar_books_node2vec[book]:
            f.write(f'{str(result[0])[38:]}\n')
        f.write('\n')

'''
These results are based on the new graph:

Split Sizes:
Total Edges: 2399
Training Set: 1919
Validation Set: 239
Test Set: 241

 Negative Sample Sizes:
Train Negatives: 1919
Validation Negatives: 239
Test Negatives: 241

AUC Score before hyper-parameter tuning: 0.5778

Final AUC Score with deepwalk: 0.9431
Hit@10: 0.5789
Hit@5: 0.5789
Hit@3: 0.4211
Hit@1: 0.3158
MRR: 0.3882
NDCG@10: 0.4143

Final AUC Score of model with biased random walk: 0.6420
Hit@10: 0.5263
Hit@5: 0.5263
Hit@3: 0.3684
Hit@1: 0.3684
MRR: 0.4079
NDCG@10: 0.4104

Final AUC Score of hybrid model: 0.8724
Results of the hybrid model: 
Hit@10: 0.5789
Hit@5: 0.5789
Hit@3: 0.3684
Hit@1: 0.3158
MRR: 0.3850
NDCG@10: 0.4162

for Node2Vec: {'walk_length': 60, 'num_walks': 15, 'dimensions': 128, 'window_size': 20, 'p': 1.0, 'q': 0.25}
'''


