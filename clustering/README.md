# Clustering / Customer Segmentation

## Scenario

`generate_data.py` builds a synthetic customer base described by recency,
frequency, and monetary value (classic RFM) plus average order value — drawn
from a mix of underlying segments the generator knows about but you don't.

## Objective

Recover sensible customer segments from the data alone, and profile each one
in business terms.

## Tasks (`analysis.py`)

1. EDA + scale the features (clustering is distance-based — scaling matters).
2. Use the **elbow method** and **silhouette score** to pick k for K-means.
3. Fit K-means at your chosen k. Profile each cluster: mean RFM values, size,
   and a plain-English name for each segment (e.g. "lapsed high-value",
   "frequent low-spend").
4. Fit hierarchical (agglomerative) clustering and compare the resulting
   segments to K-means — same story, different story?
5. Visualize the clusters in 2D (PCA or just two of the raw features) with
   distinct colors per cluster.

## Stretch goals

- Try DBSCAN and see whether it finds outlier/noise customers that K-means
  forces into a cluster anyway.
- Check cluster stability: re-run K-means with different random seeds / a
  bootstrap sample — do you get the same segments back?
- Turn each segment into a one-line marketing recommendation.

## What I found

_(fill in after you finish)_
