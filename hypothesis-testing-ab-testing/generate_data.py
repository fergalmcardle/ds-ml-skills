"""Simulates a randomized A/B test on checkout-button conversion.

Ground truth (don't peek before you've drawn your own conclusion in analysis.py):
  control conversion rate  = 8.0%
  treatment true lift      = +1.2 percentage points (relative lift ~15%)
"""
import numpy as np
import pandas as pd
from pathlib import Path

RNG_SEED = 42
N_PER_GROUP = 6000
CONTROL_RATE = 0.080
TRUE_LIFT_PP = 0.012  # treatment - control, in percentage points

OUT_PATH = Path(__file__).parent / "data" / "ab_test.csv"


def main():
    rng = np.random.default_rng(RNG_SEED)

    n = N_PER_GROUP * 2
    group = rng.choice(["control", "treatment"], size=n)

    device = rng.choice(["mobile", "desktop", "tablet"], size=n, p=[0.55, 0.35, 0.10])
    browser = rng.choice(["chrome", "safari", "firefox", "other"], size=n, p=[0.5, 0.3, 0.1, 0.1])

    base_rate = np.where(group == "control", CONTROL_RATE, CONTROL_RATE + TRUE_LIFT_PP)
    converted = rng.binomial(1, base_rate)

    df = pd.DataFrame({
        "visitor_id": np.arange(1, n + 1),
        "group": group,
        "device": device,
        "browser": browser,
        "converted": converted,
    })

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
