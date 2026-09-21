"""Simulates a housing price dataset with one nonlinear term and one
deliberately irrelevant feature (to see if Lasso finds it)."""
import numpy as np
import pandas as pd
from pathlib import Path

RNG_SEED = 11
N = 2000

OUT_PATH = Path(__file__).parent / "data" / "housing.csv"


def main():
    rng = np.random.default_rng(RNG_SEED)

    sqft = rng.normal(1800, 500, N).clip(400, 6000)
    bedrooms = rng.integers(1, 6, N)
    age_years = rng.integers(0, 80, N)
    neighborhood_quality = rng.uniform(1, 10, N)  # 1=low, 10=high
    has_garage = rng.choice([0, 1], N, p=[0.35, 0.65])
    noise_feature = rng.normal(0, 1, N)  # irrelevant, should get ~0 coefficient

    price = (
        50_000
        + 120 * sqft
        + 8_000 * bedrooms
        - 400 * age_years
        + 15_000 * neighborhood_quality
        + 10_000 * has_garage
        + 0.02 * (sqft - 1800) ** 2  # mild nonlinearity at the extremes
        + rng.normal(0, 25_000, N)  # noise
    )
    price = price.clip(50_000, None)

    df = pd.DataFrame({
        "sqft": sqft.round(0),
        "bedrooms": bedrooms,
        "age_years": age_years,
        "neighborhood_quality": neighborhood_quality.round(2),
        "has_garage": has_garage,
        "noise_feature": noise_feature.round(3),
        "price": price.round(0),
    })

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
