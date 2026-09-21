# Logistic Regression

## Scenario

`generate_data.py` builds a synthetic subscription-churn dataset: usage
frequency, tenure, support tickets, monthly price, and a contract type —
driving a binary churn outcome. Churn is deliberately imbalanced (~15% churn
rate), like a real product would look.

## Objective

Build a churn classifier and be able to explain it in business terms
(who's at risk, and why).

## Tasks (`analysis.py`)

1. EDA: churn rate overall and by contract type; class balance.
2. Train/test split (stratified, given the imbalance).
3. Fit logistic regression. Convert coefficients to **odds ratios** and
   explain at least three of them in plain English.
4. Evaluate with more than accuracy: precision, recall, F1, ROC-AUC,
   and a confusion matrix. Explain why accuracy alone would be misleading
   here.
5. Try adjusting the classification threshold away from 0.5 — how does
   precision/recall trade off? What threshold would you pick if the business
   cost of missing a churner is higher than the cost of a false alarm?
6. Handle the class imbalance explicitly (e.g. `class_weight="balanced"` or
   oversampling) and compare to the unweighted model.

## Stretch goals

- Plot a calibration curve — are the predicted probabilities trustworthy as
  probabilities, or just as a ranking?
- Add an interaction term (e.g. tenure × contract type) and see if it helps.
- Compare to a simple random forest as a non-linear baseline; discuss the
  interpretability trade-off.

## What I found

_(fill in after you finish)_
