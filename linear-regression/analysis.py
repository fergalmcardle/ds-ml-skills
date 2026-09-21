"""Starter script for the linear regression exercise. Fill in the TODOs.

Run generate_data.py first: `python generate_data.py`
"""
import pandas as pd
import numpy as np
# TODO: import what you need, e.g.
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression, Ridge, Lasso
# from sklearn.metrics import mean_squared_error, r2_score
# from statsmodels.stats.outliers_influence import variance_inflation_factor
# import statsmodels.api as sm

DATA_PATH = "data/housing.csv"
TARGET = "price"


def load_data(path=DATA_PATH):
    return pd.read_csv(path)


def train_test_split_xy(df, target=TARGET, test_size=0.2, random_state=0):
    """TODO: split into X_train, X_test, y_train, y_test."""
    raise NotImplementedError


def fit_ols(X_train, y_train):
    """TODO: fit a plain linear regression."""
    raise NotImplementedError


def fit_ridge(X_train, y_train, alpha=1.0):
    """TODO: fit Ridge regression."""
    raise NotImplementedError


def fit_lasso(X_train, y_train, alpha=1.0):
    """TODO: fit Lasso regression."""
    raise NotImplementedError


def evaluate(model, X_test, y_test):
    """TODO: return dict with rmse and r2."""
    raise NotImplementedError


def check_diagnostics(model, X_train, y_train):
    """TODO: residual plot, QQ plot, VIF per feature. Save plots or just show()."""
    raise NotImplementedError


def main():
    df = load_data()
    X_train, X_test, y_train, y_test = train_test_split_xy(df)

    ols = fit_ols(X_train, y_train)
    ridge = fit_ridge(X_train, y_train)
    lasso = fit_lasso(X_train, y_train)

    for name, model in [("OLS", ols), ("Ridge", ridge), ("Lasso", lasso)]:
        print(name, evaluate(model, X_test, y_test))

    check_diagnostics(ols, X_train, y_train)


if __name__ == "__main__":
    main()
