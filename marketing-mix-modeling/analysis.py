"""Starter script for the marketing mix modeling exercise. Fill in the TODOs.

Run generate_data.py first: `python generate_data.py`
"""
import pandas as pd
import numpy as np
# TODO: import what you need, e.g.
# from sklearn.linear_model import LinearRegression, Ridge
# import matplotlib.pyplot as plt

DATA_PATH = "data/mmm_weekly.csv"
CHANNELS = ["tv", "paid_search", "paid_social", "display"]


def load_data(path=DATA_PATH):
    return pd.read_csv(path, parse_dates=["week"])


def adstock(spend, decay):
    """TODO: geometric adstock transform.
    effective[t] = spend[t] + decay * effective[t-1]
    """
    raise NotImplementedError


def saturate(x, k, alpha):
    """TODO: diminishing-returns transform, e.g. Hill function
    x**alpha / (x**alpha + k**alpha)
    """
    raise NotImplementedError


def build_transformed_features(df, decay_by_channel, sat_params_by_channel):
    """TODO: for each channel, apply adstock then saturation using the given
    per-channel parameters. Return a DataFrame of transformed channel
    features ready to put in a regression, alongside price/promo/seasonality.
    """
    raise NotImplementedError


def fit_mmm(X, y):
    """TODO: fit a regression (start with plain linear regression) of sales
    on the transformed features.
    """
    raise NotImplementedError


def decompose_contributions(model, X):
    """TODO: use the fitted coefficients to compute each channel's total
    contribution to predicted sales (coefficient * transformed feature,
    summed over weeks). Return a per-channel contribution total.
    """
    raise NotImplementedError


def estimate_roi(contributions, df, channels=CHANNELS):
    """TODO: contribution_total / total_spend per channel."""
    raise NotImplementedError


def main():
    df = load_data()

    # TODO: pick starting decay/saturation params per channel (guess, then tune)
    decay_by_channel = {ch: 0.3 for ch in CHANNELS}
    sat_params_by_channel = {ch: dict(k=8000, alpha=1.0) for ch in CHANNELS}

    X = build_transformed_features(df, decay_by_channel, sat_params_by_channel)
    y = df["sales"]

    model = fit_mmm(X, y)
    contributions = decompose_contributions(model, X)
    print(estimate_roi(contributions, df))


if __name__ == "__main__":
    main()
