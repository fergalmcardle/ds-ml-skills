"""Simulates weekly marketing mix data with adstock + saturation dynamics.

Ground truth (don't peek before drawing your own conclusion):
  - TV has the slowest decay (long carryover) but saturates fast (small budget headroom)
  - Paid search has almost no carryover but barely saturates (scales well)
  - Paid social is in between
  - Display is the weakest channel (low true effectiveness)
"""
import numpy as np
import pandas as pd
from pathlib import Path

RNG_SEED = 5
N_WEEKS = 156  # 3 years

OUT_PATH = Path(__file__).parent / "data" / "mmm_weekly.csv"

TRUE_PARAMS = {
    "tv":           dict(decay=0.6, sat_k=8000, sat_alpha=1.2, effect=1.0),
    "paid_search":  dict(decay=0.1, sat_k=20000, sat_alpha=0.8, effect=0.9),
    "paid_social":  dict(decay=0.35, sat_k=6000, sat_alpha=1.0, effect=0.7),
    "display":      dict(decay=0.3, sat_k=5000, sat_alpha=1.0, effect=0.3),
}


def adstock(spend, decay):
    out = np.zeros_like(spend)
    carry = 0.0
    for t, s in enumerate(spend):
        carry = s + decay * carry
        out[t] = carry
    return out


def saturate(x, k, alpha):
    return x ** alpha / (x ** alpha + k ** alpha) if (x > 0).any() else x


def main():
    rng = np.random.default_rng(RNG_SEED)
    weeks = pd.date_range("2023-01-02", periods=N_WEEKS, freq="W-MON")

    spend = {
        "tv": rng.uniform(2000, 15000, N_WEEKS),
        "paid_search": rng.uniform(1000, 10000, N_WEEKS),
        "paid_social": rng.uniform(500, 8000, N_WEEKS),
        "display": rng.uniform(500, 6000, N_WEEKS),
    }

    price = 49.99 + rng.normal(0, 2, N_WEEKS)
    promo = rng.choice([0, 1], N_WEEKS, p=[0.85, 0.15])
    seasonality = 5000 * np.sin(2 * np.pi * np.arange(N_WEEKS) / 52) + 3000 * (
        pd.Series(weeks).dt.month.isin([11, 12]).astype(int)
    )

    base_sales = 40000
    contribution_total = np.zeros(N_WEEKS)
    channel_effective = {}
    for ch, params in TRUE_PARAMS.items():
        stocked = adstock(spend[ch], params["decay"])
        sat = saturate(stocked, params["sat_k"], params["sat_alpha"])
        contribution = params["effect"] * 30000 * sat
        channel_effective[ch] = contribution
        contribution_total += contribution

    sales = (
        base_sales
        + contribution_total
        + seasonality
        - 300 * (price - 49.99)
        + 8000 * promo
        + rng.normal(0, 3000, N_WEEKS)
    ).clip(0, None)

    df = pd.DataFrame({"week": weeks, "sales": sales.round(0)})
    for ch in TRUE_PARAMS:
        df[f"{ch}_spend"] = spend[ch].round(0)
    df["price"] = price.round(2)
    df["promo"] = promo

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
