"""Starter script for the A/B testing exercise. Fill in the TODOs.

Run generate_data.py first: `python generate_data.py`
"""
import pandas as pd
import numpy as np
# TODO: import what you need, e.g.
# from statsmodels.stats.proportion import proportions_ztest, proportion_confint
# from statsmodels.stats.power import NormalIndPower
# from statsmodels.stats.proportion import proportion_effectsize

DATA_PATH = "data/ab_test.csv"


def load_data(path=DATA_PATH):
    return pd.read_csv(path)


def summarize_groups(df):
    """TODO: return a small table of n, conversions, conversion rate per group."""
    raise NotImplementedError


def run_significance_test(df):
    """TODO: two-proportion z-test (or chi-squared).
    Return (statistic, p_value).
    """
    raise NotImplementedError


def confidence_interval_for_lift(df, alpha=0.05):
    """TODO: CI for (treatment_rate - control_rate)."""
    raise NotImplementedError


def required_sample_size(effect_size, alpha=0.05, power=0.80):
    """TODO: minimum sample size per group to detect `effect_size` at given
    alpha/power. Use statsmodels' NormalIndPower.solve_power or similar.
    """
    raise NotImplementedError


def main():
    df = load_data()
    print(summarize_groups(df))

    stat, p_value = run_significance_test(df)
    print(f"test statistic={stat:.3f}, p-value={p_value:.4f}")

    ci = confidence_interval_for_lift(df)
    print(f"95% CI for lift: {ci}")

    # TODO: compute the observed effect size and check power / required N
    # TODO: slice by device/browser and discuss multiple-comparisons risk in the README


if __name__ == "__main__":
    main()
