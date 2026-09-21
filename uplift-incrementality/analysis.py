"""Starter script for the uplift / incrementality exercise. Fill in the TODOs.

Run generate_data.py first: `python generate_data.py`
"""
import pandas as pd
import numpy as np
# TODO: import what you need, e.g.
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt

DATA_PATH = "data/incrementality_test.csv"
FEATURES = ["engagement_score", "tenure_months", "past_purchases_90d"]
TARGET = "purchased"
TREATMENT = "treatment"


def load_data(path=DATA_PATH):
    return pd.read_csv(path)


def average_treatment_effect(df):
    """TODO: mean(purchased | treatment=1) - mean(purchased | treatment=0)."""
    raise NotImplementedError


def fit_t_learner(df):
    """TODO: fit one classifier on df[df.treatment==1], one on
    df[df.treatment==0], both predicting `purchased` from FEATURES.
    Return (model_treated, model_control).
    """
    raise NotImplementedError


def t_learner_uplift(model_treated, model_control, X):
    """TODO: predicted P(purchase) from model_treated minus model_control,
    per row of X. This is the estimated individual uplift.
    """
    raise NotImplementedError


def fit_s_learner(df):
    """TODO: fit one classifier on everyone, using FEATURES + treatment as
    input columns.
    """
    raise NotImplementedError


def s_learner_uplift(model, X):
    """TODO: predict with treatment column forced to 1, then forced to 0,
    return the difference.
    """
    raise NotImplementedError


def qini_curve(df, uplift_scores):
    """TODO: sort customers by predicted uplift descending, compute
    cumulative incremental purchases captured (treatment - control, within
    the top-k) vs. % of population targeted. Compare to the random-targeting
    diagonal.
    """
    raise NotImplementedError


def main():
    df = load_data()
    print("Overall ATE:", average_treatment_effect(df))

    model_t, model_c = fit_t_learner(df)
    df["uplift_t_learner"] = t_learner_uplift(model_t, model_c, df[FEATURES])

    s_model = fit_s_learner(df)
    df["uplift_s_learner"] = s_learner_uplift(s_model, df[FEATURES])

    qini_curve(df, df["uplift_t_learner"])

    # TODO: identify "sure things" (high base prob, low uplift) and
    # "lost causes" (low base prob, low uplift) segments


if __name__ == "__main__":
    main()
