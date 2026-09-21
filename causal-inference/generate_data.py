"""Simulates confounded observational data for a loyalty-app opt-in.

Ground truth (don't peek before drawing your own conclusion):
  true causal effect of opt-in on 30-day spend = +$15
  engagement_score confounds both treatment assignment and outcome, so the
  naive (unadjusted) comparison will overstate the effect.
"""
import numpy as np
import pandas as pd
from pathlib import Path

RNG_SEED = 7
N = 5000
TRUE_EFFECT = 15.0

OUT_PATH = Path(__file__).parent / "data" / "loyalty_opt_in.csv"


def main():
    rng = np.random.default_rng(RNG_SEED)

    # Confounder: engagement score (unobserved by the business at decision time,
    # but observed by us as analysts via app-usage logs)
    engagement = rng.normal(50, 15, N).clip(0, 100)
    tenure_months = rng.integers(1, 60, N)

    # Treatment assignment depends on engagement (self-selection into opt-in)
    propensity = 1 / (1 + np.exp(-(engagement - 50) / 10))
    treatment = rng.binomial(1, propensity)

    # Outcome depends on engagement, tenure, AND the true causal effect of treatment
    noise = rng.normal(0, 10, N)
    spend = (
        20
        + 1.5 * engagement
        + 0.3 * tenure_months
        + TRUE_EFFECT * treatment
        + noise
    )

    df = pd.DataFrame({
        "customer_id": np.arange(1, N + 1),
        "engagement_score": engagement.round(1),
        "tenure_months": tenure_months,
        "opted_in": treatment,
        "spend_30d": spend.round(2),
    })

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
