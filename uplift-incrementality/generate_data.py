"""Simulates a randomized incrementality test with heterogeneous treatment
effect (uplift depends on customer features).

Ground truth (don't peek before drawing your own conclusion):
  - High-engagement, mid-tenure customers have the biggest true uplift
  - Already-frequent buyers ("sure things") have ~zero true uplift -- they'd
    buy anyway, so the discount is wasted on them
  - Very low engagement customers ("lost causes") also have ~zero uplift --
    the discount isn't enough to move them
"""
import numpy as np
import pandas as pd
from pathlib import Path

RNG_SEED = 17
N = 8000

OUT_PATH = Path(__file__).parent / "data" / "incrementality_test.csv"


def true_uplift(engagement, tenure_months):
    # peaks at mid engagement & mid tenure, ~0 at the extremes
    eng_term = np.exp(-((engagement - 55) ** 2) / (2 * 20 ** 2))
    tenure_term = np.exp(-((tenure_months - 18) ** 2) / (2 * 12 ** 2))
    return 0.25 * eng_term * tenure_term  # max ~0.25 probability lift


def main():
    rng = np.random.default_rng(RNG_SEED)

    engagement = rng.uniform(0, 100, N)
    tenure_months = rng.uniform(0, 48, N)
    past_purchases_90d = rng.poisson(2, N)

    treatment = rng.binomial(1, 0.5, N)  # randomized

    base_prob = 0.10 + 0.002 * past_purchases_90d
    uplift = true_uplift(engagement, tenure_months)
    prob_purchase = np.clip(base_prob + treatment * uplift, 0, 1)
    purchased = rng.binomial(1, prob_purchase)

    df = pd.DataFrame({
        "customer_id": np.arange(1, N + 1),
        "engagement_score": engagement.round(1),
        "tenure_months": tenure_months.round(1),
        "past_purchases_90d": past_purchases_90d,
        "treatment": treatment,
        "purchased": purchased,
    })

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
