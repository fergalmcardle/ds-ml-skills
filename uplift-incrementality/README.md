# Uplift Modeling / Incrementality

## Scenario

A randomized incrementality test: customers were randomly assigned to receive
a discount offer (treatment) or not (control). Unlike the basic A/B test
folder, here the **effect size varies by customer** (heterogeneous treatment
effect) — some segments respond strongly, some barely react, and a few would
have bought anyway (the offer is wasted spend on them).

## Objective

Go beyond "did it work on average" to "who should we target with this offer
next time" — i.e. estimate individual/segment-level uplift, not just the
overall average treatment effect.

## Tasks (`analysis.py`)

1. Start with the overall average treatment effect (treatment mean − control
   mean), same as a basic A/B test — this is your floor/baseline.
2. Build a **T-learner**: fit one model on treatment-group data
   (predict outcome from features), one model on control-group data, and take
   the difference in predictions per customer as their estimated uplift.
3. Build an **S-learner** for comparison: one model trained on everyone with
   treatment as a feature; predict twice per customer (treatment=1 and
   treatment=0) and take the difference.
4. Rank customers by estimated uplift and compute a **Qini curve** (cumulative
   incremental outcome captured vs. % of customers targeted, ordered by
   predicted uplift) — compare to random targeting.
5. Identify the segment(s) with negative or near-zero uplift ("sure things"
   or "lost causes" in uplift-modeling terms) — these are the customers you'd
   stop targeting to save spend.

## Stretch goals

- Compare T-learner vs. S-learner rankings — do they agree on who the
  best/worst targets are?
- If you want to go further, look into `sklift` or `causalml` (separate
  install) for a proper uplift-tree implementation, and compare to your
  from-scratch T-learner.

## What I found

_(fill in after you finish)_
