"""This exercise uses REAL data (sklearn's bundled `digits` dataset), so
there's nothing to generate. This script just confirms the data loads and
caches a CSV copy in data/ for convenience/inspection.
"""
from pathlib import Path
import pandas as pd
from sklearn.datasets import load_digits

OUT_PATH = Path(__file__).parent / "data" / "digits.csv"


def main():
    digits = load_digits()
    df = pd.DataFrame(digits.data, columns=[f"pixel_{i}" for i in range(digits.data.shape[1])])
    df["label"] = digits.target

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUT_PATH} (8x8 images, 64 pixel features + label)")


if __name__ == "__main__":
    main()
