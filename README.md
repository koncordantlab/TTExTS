# T-TExTS: Teaching Text Expansion for Teacher Scaffolding

**Enhancing Text Selection in High School Literature through Knowledge Graph-Based Recommendation**

This repository contains the code, data, and ontology for T-TExTS, a knowledge graph (KG)-based recommendation system that helps high school English teachers build **text sets**: groups of thematically aligned literary works taught together to deepen students' understanding of a topic.

Published in *Data Mining and Knowledge Discovery* (2026), 40:70.
[https://doi.org/10.1007/s10618-026-01228-5](https://doi.org/10.1007/s10618-026-01228-5)

## Citation

If you use T-TExTS in your work, please cite:

> Gelal, N., Snow, C., Rios, A., Jagodnik, K. M., & McGinty, H. K. (2026). T-TExTS (teaching text
> expansion for teacher scaffolding): Enhancing text selection in high school literature through
> knowledge graph-based recommendation. *Data Mining and Knowledge Discovery*, 40(5), 70.
> https://doi.org/10.1007/s10618-026-01228-5

```bibtex
@article{gelal2026t,
  title={T-TExTS (teaching text expansion for teacher scaffolding): Enhancing text selection in high school literature through knowledge graph-based recommendation},
  author={Gelal, Nirmal and Snow, Chloe and Rios, Ambyr and Jagodnik, Kathleen M and McGinty, Hande K{\"u}{\c{c}}{\"u}k},
  journal={Data Mining and Knowledge Discovery},
  volume={40},
  number={5},
  pages={70},
  year={2026},
  publisher={Springer}
}
```

## Authors

Nirmal Gelal¹, Chloe Snow², Ambyr Rios², Kathleen M. Jagodnik¹, Hande Küçük McGinty¹

¹ Department of Computer Science, Kansas State University
² Department of Curriculum and Instruction, Kansas State University

Contact: Hande Küçük McGinty — hande@ksu.edu

## What problem does this solve?

High school English teachers often lack the planning time, materials, and pedagogical training needed to assemble diverse, thematically coherent text sets. As a result, the texts actually taught have remained largely unchanged for a century: familiar, canonical, and frequently mismatched with students' identities and interests.

T-TExTS recommends texts based on **pedagogical merit** rather than surface-level metadata or popularity. Given an anchor text a teacher already uses, it suggests works that are *diverse* in genre, theme, subtheme, and author, yet *similar* in pedagogical merit and text complexity.

## How it works

1. **Pedagogy-grounded ontology.** A domain-specific ontology for high school English Literature built with the Knowledge Acquisition and Representation Methodology (KNARM), through iterative interviews and validation with English Language Arts teachers and teacher educators. It models not only genre, theme, and author, but also qualitative pedagogical elements — levels of meaning, text structure, language conventionality and clarity, and knowledge demands — alongside quantitative complexity measures (Lexile, Flesch-Kincaid, ATOS).

2. **Knowledge graph.** The ontology is instantiated as an RDF knowledge graph with a shared schema-level TBox (classes such as `Text`, `Author`, `Genre`, `Theme`, `TextComplexity`) and a per-dataset ABox of assertions (`has_author`, `has_genre`, `has_theme`, ...). Three configurations of increasing scale were curated: **98, 196, and 351 texts**.

3. **Graph embeddings.** Random walks over the graph are treated as sentences and embedded with skip-gram (Word2Vec). Four strategies are compared:
   - **DeepWalk** — uniform random walks
   - **Biased random walk** — transition probabilities weighted by domain-expert-assigned relation importance
   - **Hybrid** — concatenation of DeepWalk and biased random walk embeddings
   - **Node2Vec** — parameterized walks balancing BFS/DFS exploration via `p` and `q`

4. **Recommendation.** Cosine similarity over the learned embeddings produces a ranked top-*n* list of pedagogically related texts for any anchor text.

Hyperparameters were tuned with Optuna (50 trials per model per dataset size), using link-prediction AUC on a validation split as the objective. Evaluation uses AUC, Hits@K, MRR, and nDCG@10 against expert-curated ground truth.

## Key findings

- **Traversal-level expert weighting alone does not beat algorithmic structural tuning.** Node2Vec — which applies no extra weighting at traversal time — achieves the highest AUC at every dataset  size (**0.9642–0.9750**) and the strongest ranking metrics on the larger graphs.
- **Combining the two signals works best in practice.** The hybrid embedding holds a high AUC across all scales (**0.9122–0.9350**) while staying within a few percentage points of Node2Vec on every ranking metric, *and* exposes which expert weights shaped the result — the transparency a teacher-facing tool needs.
- **The pedagogy already lives in the graph.** All four models traverse the same expert-curated ontology, so the pedagogical signal is encoded structurally; additional traversal-level weighting is unnecessary and can cost structural coverage. This validates the ontology design.
- **Stable across scale.** AUC barely moves as the graph grows from 868 to 1,312 entities, suggesting the expert-curated structure generalizes as a curriculum expands.
- **Depth beats locality.** Optuna independently selected the maximum `q = 4.0` for Node2Vec at every dataset size, indicating that the most useful pedagogical signal lies in longer chains of association through intermediate concepts rather than in tight local neighborhoods.

For the anchor text *1984*, Node2Vec was the only configuration to recover all five expert ground-truth recommendations (*Fahrenheit 451*, *Brave New World*, *Animal Farm*, *The Hunger Games*, *Marrow Thieves*) in its top 10. Consistent near-misses across models — *The Giver*, *The Pedestrian*, *Scythe* — are pedagogically defensible companions that standard ranking metrics penalize.

## Project structure

```
.
├── data/                          Datasets, ontologies, graphs, trained models, and outputs
│   ├── book_data_{98,196,351}.csv     Curated text metadata for each dataset configuration
│   ├── ground_truth_{19,39,65}.csv    Expert-curated ground-truth recommendations
│   ├── owls/                          OWL ontologies: genre, theme, and subtheme modules plus the full TBox + ABox output per dataset size
│   ├── graphs/                        Serialized NetworkX / DeepWalk graphs per dataset size
│   ├── models/                        Tuned embedding models with their best hyperparameters
│   └── recommendations/               Final top-n recommendations per model and weight config
│
├── kg/                            Ontology and knowledge graph construction (RDFLib)
│   ├── genre.py                       Genre taxonomy module
│   ├── theme.py                       Theme taxonomy module
│   ├── subtheme.py                    Subtheme taxonomy module
│   └── createKG.ipynb                 Assembles the modules into the full knowledge graph
│
├── utils/                         Shared helpers
│   ├── __init__.py
│   └── utils.py                       Text cleaning, year normalization, device setup, logging
│
├── data_prep.py                   Graph loading and 80/10/10 train/val/test edge splits
├── negative_sampler.py            Negative triple generation with positive-triple filtering
├── deepwalk_trainer.py            DeepWalk (uniform random walk) embeddings
├── biased_random_walker.py        Domain-expert-weighted biased random walk
├── node2vec_trainer.py            Node2Vec (parameterized random walk) embeddings
├── hybrid.py                      Hybrid embedding via concatenation of DeepWalk + biased RW
├── hyper_parameter_tuner.py       Optuna hyperparameter search (link-prediction AUC objective)
├── link_predictor.py              Evaluation: AUC, Hits@K, MRR, nDCG@10
└── new_main.py                    Full experiment sweep across dataset sizes, weight configurations, and all four embedding models
```

Running `new_main.py` reproduces the full evaluation, writing aggregated results to
`data/results/` and run logs to `data/logs/` (both created at runtime).

## License

The paper is published Open Access under
[CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).
Source code is also available at [koncordantlab/TTExTS](https://github.com/koncordantlab/TTExTS).
