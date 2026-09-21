# Dimensionality Reduction

## Scenario

This one uses **real data**: scikit-learn's bundled `digits` dataset
(8x8 grayscale images of handwritten digits 0-9, 1797 samples, 64 features) —
no download required, it ships with sklearn.

## Objective

Understand what PCA actually buys you: how much variance can you throw away
before the structure disappears, and can you *see* the digit classes separate
out in 2D even though you never told the algorithm the labels?

## Tasks (`analysis.py`)

1. Load the digits dataset (`sklearn.datasets.load_digits`). Note: don't use
   `generate_data.py` here — see the note in that file.
2. Standardize the pixel features, run PCA keeping all components.
3. Plot cumulative explained variance vs. number of components. How many
   components do you need for 90%/95% of the variance?
4. Reduce to 2 components and scatter-plot, colored by the true digit label
   (label is only used for coloring/verification, not for fitting PCA).
   Do the digit classes visually separate?
5. Reconstruct the images from a low-dimensional PCA representation (e.g. 10
   components) and visually compare a few reconstructed digits to the
   originals — how much detail is lost?

## Stretch goals

- Compare PCA's 2D embedding to t-SNE's (`sklearn.manifold.TSNE`) on the same
  data — which separates the classes more cleanly, and why might that be
  (hint: PCA is linear/global, t-SNE is nonlinear/local)?
- Feed the PCA-reduced features (e.g. top 20 components) into a simple
  classifier (e.g. logistic regression or kNN) and compare accuracy/speed to
  using the raw 64 features.

## What I found

_(fill in after you finish)_
