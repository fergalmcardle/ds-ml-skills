# Causal Inference (Observational Data)

## Scenario

A retailer rolled out a loyalty-app push-notification feature, but **not**
randomly — customers who were already more engaged were more likely to opt in
(self-selection / confounding). `generate_data.py` simulates this: engagement
level confounds both "opted in" (treatment) and "30-day spend" (outcome).

## Objective

Estimate the **causal** effect of opting in on spend, and show why the naive
comparison is misleading.

## Tasks (`analysis.py`)

1. Naive estimate: mean spend, opted-in vs not. This is biased — say why.
2. Regression adjustment: control for the confounder(s) directly in an OLS
   model. Compare the adjusted effect to the naive one.
3. Propensity score matching: estimate P(treatment | confounders), match
   treated/control units on propensity score, re-estimate the effect.
4. Inverse propensity weighting (IPW) as a second way to adjust — compare to
   matching.
5. Check overlap/common support: are there confounder values where only
   treated or only control units exist? What would you do about it?
6. Compare all four estimates (naive, regression, PSM, IPW) side by side and
   discuss which you'd trust and why.

## Stretch goals

- Add an unobserved confounder to the generator and see how much your
  estimates break — this is the core limitation of everything above (they
  only handle *observed* confounding).
- Try difference-in-differences: extend the generator to include a
  pre/post period and a staggered rollout, then estimate the DiD effect.
- Read up on and briefly note (in this README) what an instrumental variable
  would need to look like for this scenario, even if you don't implement it.

## What I found

_(fill in after you finish)_
