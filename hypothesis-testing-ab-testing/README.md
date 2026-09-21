# Hypothesis Testing & A/B Testing

## Scenario

You work at an e-commerce company. Product shipped a new checkout button (treatment)
against the old one (control) in a randomized experiment. `generate_data.py` simulates
the raw event log: one row per visitor, with a random assignment and a (secretly
known-to-the-generator) true lift so you can check your answer at the end.

## Objective

Decide whether the new button actually improves conversion, and how confident you
should be in that decision.

## Tasks (`analysis.py`)

1. Load the data, compute conversion rate by group, sanity-check sample sizes.
2. Run a two-proportion z-test (or chi-squared test) — get a p-value.
3. Compute a confidence interval for the difference in conversion rates.
4. Run a **power analysis**: given the observed effect size, was this experiment
   even sized to detect it? Compute the minimum sample size needed for 80% power.
5. Check the multiple-comparisons trap: what if you'd also cut the data by device
   type and browser? Discuss (in the README) why peeking at many slices inflates
   false-positive risk, and what you'd do about it (Bonferroni, pre-registration,
   sequential testing).
6. Sanity check: does your conclusion match the true lift baked into
   `generate_data.py`? (Open the script after you're done — not before.)

## Stretch goals

- Re-run as a sequential test (e.g. simple SPRT or alpha-spending) instead of a
  fixed-horizon test.
- Add a guardrail metric (e.g. revenue per visitor) and check for a regression
  even if conversion improves.
- Try a Bayesian A/B test (Beta-Binomial) and compare conclusions/intuition to
  the frequentist result.

## What I found

_(fill in after you finish — 3-5 sentences: what the data showed, how confident
you are, and what you'd tell a stakeholder)_
