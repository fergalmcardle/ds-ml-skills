"""Starter script for the causal inference exercise. Fill in the TODOs.

Run generate_data.py first: `python generate_data.py`
"""
import pandas as pd
import numpy as np
# TODO: import what you need, e.g.
# import statsmodels.formula.api as smf
# from sklearn.linear_model import LogisticRegression
# from sklearn.neighbors import NearestNeighbors

DATA_PATH = "data/loyalty_opt_in.csv"


def load_data(path=DATA_PATH):
    return pd.read_csv(path)


def naive_effect(df):
    """TODO: mean spend for opted_in==1 minus mean spend for opted_in==0."""
    raise NotImplementedError


def regression_adjusted_effect(df):
    """TODO: OLS of spend_30d ~ opted_in + engagement_score + tenure_months.
    Return the coefficient on opted_in.
    """
    raise NotImplementedError


def estimate_propensity_scores(df):
    """TODO: logistic regression of opted_in ~ engagement_score + tenure_months.
    Return predicted probabilities (propensity scores).
    """
    raise NotImplementedError


def psm_effect(df, propensity_scores):
    """TODO: nearest-neighbor match treated to control units on propensity
    score, then compare mean outcome within matched pairs.
    """
    raise NotImplementedError


def ipw_effect(df, propensity_scores):
    """TODO: inverse propensity weighting estimate of the average treatment
    effect. Watch for extreme weights near 0 or 1.
    """
    raise NotImplementedError


def main():
    df = load_data()

    print("Naive effect:", naive_effect(df))
    print("Regression-adjusted effect:", regression_adjusted_effect(df))

    ps = estimate_propensity_scores(df)
    print("PSM effect:", psm_effect(df, ps))
    print("IPW effect:", ipw_effect(df, ps))

    # TODO: check common support / overlap of propensity scores between groups


if __name__ == "__main__":
    main()
