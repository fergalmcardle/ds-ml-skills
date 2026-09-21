"""Simulates RFM (recency/frequency/monetary) customer data drawn from a
mix of latent segments. The segment labels are dropped from the output --
that's what you're trying to recover via clustering."""
import numpy as np
import pandas as pd
from pathlib import Path

RNG_SEED = 21
N = 1500

OUT_PATH = Path(__file__).parent / "data" / "customers.csv"

# (recency_days mean/sd, frequency mean/sd, monetary mean/sd, avg_order_value mean/sd)
SEGMENTS = {
    "champions": dict(recency=(10, 5), frequency=(20, 5), monetary=(2000, 400), aov=(100, 20)),
    "at_risk_high_value": dict(recency=(180, 30), frequency=(15, 4), monetary=(1500, 300), aov=(100, 25)),
    "frequent_low_spend": dict(recency=(20, 8), frequency=(18, 5), monetary=(300, 80), aov=(17, 5)),
    "new_low_engagement": dict(recency=(15, 10), frequency=(2, 1), monetary=(80, 30), aov=(40, 10)),
    "lapsed": dict(recency=(300, 40), frequency=(3, 1), monetary=(150, 50), aov=(50, 15)),
}


def main():
    rng = np.random.default_rng(RNG_SEED)
    segment_names = rng.choice(list(SEGMENTS.keys()), N, p=[0.15, 0.15, 0.2, 0.25, 0.25])

    rows = []
    for seg in segment_names:
        p = SEGMENTS[seg]
        recency = max(1, rng.normal(*p["recency"]))
        frequency = max(1, rng.normal(*p["frequency"]))
        monetary = max(10, rng.normal(*p["monetary"]))
        aov = max(5, rng.normal(*p["aov"]))
        rows.append((recency, frequency, monetary, aov))

    df = pd.DataFrame(rows, columns=["recency_days", "frequency", "monetary", "avg_order_value"])
    df.insert(0, "customer_id", np.arange(1, N + 1))
    df = df.round(1)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUT_PATH} (true segment labels withheld on purpose)")


if __name__ == "__main__":
    main()
