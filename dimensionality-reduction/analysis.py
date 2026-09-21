"""Starter script for the dimensionality reduction exercise. Fill in the TODOs.

Run generate_data.py first (just caches the sklearn dataset to CSV):
`python generate_data.py`
"""
import pandas as pd
import numpy as np
# TODO: import what you need, e.g.
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# from sklearn.manifold import TSNE
# import matplotlib.pyplot as plt

DATA_PATH = "data/digits.csv"


def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    X = df.drop(columns=["label"]).values
    y = df["label"].values
    return X, y


def scale_features(X):
    """TODO: standardize pixel features."""
    raise NotImplementedError


def fit_pca(X_scaled, n_components=None):
    """TODO: fit PCA (all components if n_components is None)."""
    raise NotImplementedError


def plot_cumulative_variance(pca):
    """TODO: plot cumulative explained_variance_ratio_ vs component count."""
    raise NotImplementedError


def plot_2d_embedding(X_2d, y):
    """TODO: scatter plot of the first two components/dimensions, colored by y."""
    raise NotImplementedError


def reconstruct_and_compare(X_scaled, n_components, sample_indices=(0, 1, 2)):
    """TODO: fit PCA with n_components, transform + inverse_transform a few
    samples, and compare (visually or numerically) to the originals.
    """
    raise NotImplementedError


def main():
    X, y = load_data()
    X_scaled = scale_features(X)

    pca_full = fit_pca(X_scaled)
    plot_cumulative_variance(pca_full)

    pca_2d = fit_pca(X_scaled, n_components=2)
    X_2d = pca_2d.transform(X_scaled)
    plot_2d_embedding(X_2d, y)

    reconstruct_and_compare(X_scaled, n_components=10)

    # TODO (stretch): compare to TSNE's 2D embedding


if __name__ == "__main__":
    main()
