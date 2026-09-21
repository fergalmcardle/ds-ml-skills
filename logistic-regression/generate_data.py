"""Simulates a subscription-churn dataset with realistic class imbalance."""
import numpy as np
import pandas as pd
from pathlib import Path

RNG_SEED = 3
N = 4000

OUT_PATH = Path(__file__).parent / "data" / "churn.csv"


def main():
    rng = np.random.default_rng(RNG_SEED)

    tenure_months = rng.integers(1, 60, N)
    monthly_price = rng.choice([9.99, 19.99, 29.99, 49.99], N)
    usage_sessions_per_week = rng.poisson(4, N).clip(0, None)
    support_tickets_90d = rng.poisson(0.5, N).clip(0, None)
    contract_type = rng.choice(["monthly", "annual"], N, p=[0.7, 0.3])

    # Log-odds combine several realistic churn drivers
    logit = (
        -1.1
        - 0.05 * tenure_months
        + 0.30 * support_tickets_90d
        - 0.20 * usage_sessions_per_week
        + 0.02 * monthly_price
        + np.where(contract_type == "monthly", 0.8, -0.8)
    )
    prob_churn = 1 / (1 + np.exp(-logit))
    churned = rng.binomial(1, prob_churn)

    df = pd.DataFrame({
        "customer_id": np.arange(1, N + 1),
        "tenure_months": tenure_months,
        "monthly_price": monthly_price,
        "usage_sessions_per_week": usage_sessions_per_week,
        "support_tickets_90d": support_tickets_90d,
        "contract_type": contract_type,
        "churned": churned,
    })

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUT_PATH}; churn rate={df['churned'].mean():.1%}")


if __name__ == "__main__":
    main()
