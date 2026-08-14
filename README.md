# T-TExTS: Teaching Text Expansion for Teacher Scaffolding

**Enhancing Text Selection in High School Literature through Knowledge Graph-Based Recommendation**

This repository contains the code, data, and ontology for T-TExTS, a knowledge graph (KG)-based recommendation system that helps high school English teachers build **text sets**: groups of thematically aligned literary works taught together to deepen students' understanding of a topic.

Published in *Data Mining and Knowledge Discovery* (2026), 40:70.
[https://doi.org/10.1007/s10618-026-01228-5](https://doi.org/10.1007/s10618-026-01228-5)

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


## Citation

If you use T-TExTS in your work, please cite:

> Gelal, N., Snow, C., Rios, A., Jagodnik, K. M., & Küçük McGinty, H. (2026). T-TExTS (Teaching
> Text Expansion for Teacher Scaffolding): Enhancing Text Selection in High School Literature
> through Knowledge Graph-Based Recommendation. *Data Mining and Knowledge Discovery*, 40, 70.
> https://doi.org/10.1007/s10618-026-01228-5

```bibtex
@article{gelal2026ttexts,
  title   = {T-TExTS (Teaching Text Expansion for Teacher Scaffolding): Enhancing Text
             Selection in High School Literature through Knowledge Graph-Based Recommendation},
  author  = {Gelal, Nirmal and Snow, Chloe and Rios, Ambyr and
             Jagodnik, Kathleen M. and K{\"u}{\c{c}}{\"u}k McGinty, Hande},
  journal = {Data Mining and Knowledge Discovery},
  volume  = {40},
  number  = {1},
  pages   = {70},
  year    = {2026},
  doi     = {10.1007/s10618-026-01228-5}
}
```

## Authors

Nirmal Gelal¹, Chloe Snow², Ambyr Rios², Kathleen M. Jagodnik¹, Hande Küçük McGinty¹

¹ Department of Computer Science, Kansas State University
² Department of Curriculum and Instruction, Kansas State University

Contact: Hande Küçük McGinty — hande@ksu.edu

## License

The paper is published Open Access under
[CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).
Source code is also available at [koncordantlab/TTExTS](https://github.com/koncordantlab/TTExTS).
