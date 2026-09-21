# Marketing Mix Modeling (MMM)

## Scenario

`generate_data.py` simulates 3 years of weekly data: spend across 4 channels
(TV, paid search, paid social, display), plus price, a promo flag, and
seasonality — all driving weekly sales. Each channel has its own **adstock**
(carryover) and **saturation** (diminishing returns) dynamics baked in, like a
real media mix would.

## Objective

Recover each channel's contribution to sales and estimate ROI per channel,
well enough to make a "where should we shift budget" recommendation.

## Tasks (`analysis.py`)

1. EDA: plot weekly sales and each channel's spend over time. Note any
   obvious seasonality.
2. Implement an **adstock transform** (geometric decay: this week's effective
   spend = raw spend + decay_rate × last week's effective spend) for each
   channel. Try a couple of decay rates and see how the fit changes.
3. Implement a **saturation transform** (e.g. Hill function or simple log)
   on top of adstocked spend, to capture diminishing returns.
4. Fit a regression of sales on the transformed channel variables + price +
   promo + a seasonality term (e.g. month dummies or a Fourier term).
5. Decompose predicted sales into a contribution per channel (+ base sales).
   Turn each channel's total contribution and total spend into an estimated
   ROI.
6. Sanity-check against the generator's ground truth (open `generate_data.py`
   after you're done) — did you recover the right channels as strongest?

## Stretch goals

- Grid-search adstock decay and saturation parameters instead of guessing.
- Compute **response curves** per channel (predicted incremental sales vs.
  spend level) — these are what you'd actually hand to a budget-allocation
  decision.
- Compare your regression-based decomposition to what a `Ridge` model with
  the same transformed features gives you — does regularization change which
  channel looks best?

## What I found

_(fill in after you finish)_
