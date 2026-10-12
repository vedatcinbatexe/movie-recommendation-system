"""Download the MovieLens 100K dataset into data/raw/."""

import io
import urllib.request
import zipfile
from pathlib import Path

URL = "https://files.grouplens.org/datasets/movielens/ml-100k.zip"
RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def main() -> None:
    target = RAW_DIR / "ml-100k"
    if target.exists():
        print(f"Dataset already present at {target}")
        return

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {URL} ...")
    with urllib.request.urlopen(URL) as response:
        archive = zipfile.ZipFile(io.BytesIO(response.read()))
    archive.extractall(RAW_DIR)
    print(f"Extracted to {target}")


if __name__ == "__main__":
    main()
