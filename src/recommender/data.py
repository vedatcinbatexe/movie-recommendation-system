"""Loaders for the raw MovieLens 100K files."""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw" / "ml-100k"

GENRES = [
    "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy",
    "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror",
    "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western",
]


def load_ratings() -> pd.DataFrame:
    """One row per rating: user_id, movie_id, rating (1-5), timestamp."""
    ratings = pd.read_csv(
        RAW_DIR / "u.data",
        sep="\t",
        names=["user_id", "movie_id", "rating", "timestamp"],
    )
    ratings["timestamp"] = pd.to_datetime(ratings["timestamp"], unit="s")
    return ratings


def load_movies() -> pd.DataFrame:
    """One row per movie: movie_id, title, release_date and a 0/1 column per genre."""
    columns = ["movie_id", "title", "release_date", "video_release_date", "imdb_url"] + GENRES
    movies = pd.read_csv(RAW_DIR / "u.item", sep="|", names=columns, encoding="latin-1")
    movies["release_date"] = pd.to_datetime(movies["release_date"], format="%d-%b-%Y")
    return movies.drop(columns=["video_release_date", "imdb_url"])


def load_users() -> pd.DataFrame:
    """One row per user: user_id, age, gender, occupation, zip_code."""
    return pd.read_csv(
        RAW_DIR / "u.user",
        sep="|",
        names=["user_id", "age", "gender", "occupation", "zip_code"],
    )
