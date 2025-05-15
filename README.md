# T-TExTS: Teaching Text Expansion for Teacher Scaffolding

**T-TExTS** is a knowledge graph-based recommendation system that assists high school English teachers in selecting diverse, thematically aligned literature texts. It uses semantic modeling, ontology engineering, and graph embedding techniques (like DeepWalk and biased random walks) to offer high-quality textbook suggestions based on pedagogical merit and thematic relevance.

---

## 🚀 How It Works

1. **Ontology Creation**: Uses KNARM methodology to build an OWL ontology of ~100 books, annotated with pedagogical and thematic metadata.
2. **Graph Generation**: Ontology is converted to RDF triples and modeled as a knowledge graph.
3. **Embedding**: DeepWalk and biased random walks generate graph embeddings.
4. **Recommendation Engine**: Cosine similarity on embeddings identifies top-N similar texts.
5. **Evaluation**: Models are assessed using AUC, MRR, Hits@K, and nDCG metrics.

## 🛠️ Installation

```bash
git clone https://github.com/koncordantlab/TTExTS.git
cd TTExTS
python -m venv env              
source env/bin/activate        # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
```


## ▶️ Usage
To run the full pipeline:
```bash
source env/bin/activate        # if not already activated
python script/main.py
```