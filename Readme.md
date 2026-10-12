# Movie Recommendation System

Course project for Introduction to Machine Learning (YTU). It recommends movies to users
from their past ratings, comparing a popularity baseline, content-based filtering and
collaborative filtering (KNN and SVD) on the MovieLens 100K dataset.

## Setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/download_data.py
```

## Project structure

```
data/raw/           MovieLens 100K files (downloaded, not in git)
notebooks/          Exploratory analysis and experiments
scripts/            One-off scripts such as the dataset download
src/recommender/    Reusable code: data loading, models, evaluation
```

## Roadmap

- [x] Exploratory data analysis
- [ ] Load the data into PostgreSQL
- [x] Train/test split and baselines (global average, movie average, popularity list)
- [ ] Content-based filtering (genres + cosine similarity)
- [ ] Collaborative filtering (KNN, SVD)
- [ ] Evaluation: RMSE, MAE, Precision@K, Recall@K
- [ ] FastAPI endpoints
- [ ] Docker Compose (database, trainer, API)
