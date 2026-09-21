"""Starter script for the logistic regression exercise. Fill in the TODOs.

Run generate_data.py first: `python generate_data.py`
"""
import pandas as pd
import numpy as np
# TODO: import what you need, e.g.
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.metrics import (
#     classification_report, roc_auc_score, roc_curve, confusion_matrix
# )

DATA_PATH = "data/churn.csv"
TARGET = "churned"


def load_data(path=DATA_PATH):
    return pd.read_csv(path)


def prepare_features(df):
    """TODO: encode contract_type, assemble X (features) and y (target)."""
    raise NotImplementedError


def train_test_split_xy(X, y, test_size=0.2, random_state=0):
    """TODO: stratified train/test split given the class imbalance."""
    raise NotImplementedError


def fit_logistic_regression(X_train, y_train, class_weight=None):
    """TODO: fit sklearn LogisticRegression. class_weight="balanced" is one
    way to address imbalance — try both None and "balanced".
    """
    raise NotImplementedError


def coefficients_as_odds_ratios(model, feature_names):
    """TODO: exponentiate coefficients to get odds ratios; return as a
    Series/DataFrame you can print and interpret.
    """
    raise NotImplementedError


def evaluate(model, X_test, y_test, threshold=0.5):
    """TODO: precision/recall/F1/ROC-AUC/confusion matrix at the given
    threshold. Predicted probability >= threshold => predicted churn.
    """
    raise NotImplementedError


def main():
    df = load_data()
    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = train_test_split_xy(X, y)

    model = fit_logistic_regression(X_train, y_train)
    print(coefficients_as_odds_ratios(model, X.columns))
    print(evaluate(model, X_test, y_test))

    # TODO: try class_weight="balanced" and compare
    # TODO: sweep threshold values and plot the precision/recall trade-off


if __name__ == "__main__":
    main()
