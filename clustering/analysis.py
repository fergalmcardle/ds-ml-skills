"""Starter script for the clustering exercise. Fill in the TODOs.

Run generate_data.py first: `python generate_data.py`
"""
import pandas as pd
import numpy as np
# TODO: import what you need, e.g.
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
# from sklearn.metrics import silhouette_score
# from sklearn.decomposition import PCA
# import matplotlib.pyplot as plt

DATA_PATH = "data/customers.csv"
FEATURES = ["recency_days", "frequency", "monetary", "avg_order_value"]


def load_data(path=DATA_PATH):
    return pd.read_csv(path)


def scale_features(df, features=FEATURES):
    """TODO: standardize features; return the scaled array (and the scaler)."""
    raise NotImplementedError


def elbow_and_silhouette(X_scaled, k_range=range(2, 10)):
    """TODO: fit KMeans for each k in k_range, collect inertia (elbow) and
    silhouette score. Return something plottable, or just print/plot here.
    """
    raise NotImplementedError


def fit_kmeans(X_scaled, k):
    """TODO: fit KMeans with the chosen k, return the fitted model."""
    raise NotImplementedError


def profile_clusters(df, labels, features=FEATURES):
    """TODO: group by cluster label, return mean of each feature + cluster size."""
    raise NotImplementedError


def fit_hierarchical(X_scaled, k):
    """TODO: fit AgglomerativeClustering with the chosen k."""
    raise NotImplementedError


def plot_clusters_2d(X_scaled, labels):
    """TODO: PCA down to 2 components (or pick 2 raw features) and scatter,
    colored by cluster label.
    """
    raise NotImplementedError


def main():
    df = load_data()
    X_scaled = scale_features(df)

    elbow_and_silhouette(X_scaled)  # look at the output, then pick k below
    k = 5  # TODO: replace with your chosen k

    kmeans = fit_kmeans(X_scaled, k)
    print(profile_clusters(df, kmeans.labels_))

    hier = fit_hierarchical(X_scaled, k)
    print(profile_clusters(df, hier.labels_))

    plot_clusters_2d(X_scaled, kmeans.labels_)


if __name__ == "__main__":
    main()
