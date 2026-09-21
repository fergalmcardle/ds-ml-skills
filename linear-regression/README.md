# Linear Regression

## Scenario

`generate_data.py` builds a synthetic housing dataset: square footage, bedrooms,
age, neighborhood quality, and a categorical "has_garage" — driving a sale
price with realistic noise, one mildly nonlinear term, and one irrelevant
"noise" feature thrown in on purpose.

## Objective

Build a defensible price model and be able to explain what it does and doesn't
capture well.

## Tasks (`analysis.py`)

1. EDA: distributions, pairwise correlations with price, obvious outliers.
2. Train/test split. Fit a baseline OLS model.
3. Interpret coefficients — are the signs/magnitudes sensible?
4. Check regression diagnostics: residual plot (heteroscedasticity?), QQ plot
   (normality of residuals?), VIF (multicollinearity?).
5. Try Ridge and Lasso regression; compare coefficients and test-set error to
   plain OLS. Does Lasso zero out the irrelevant "noise" feature?
6. Report test-set RMSE and R² for all three models.

## Stretch goals

- Add a polynomial/interaction term for the nonlinear relationship you should
  notice during EDA — does it materially improve fit?
- Try `statsmodels` for the OLS fit specifically so you can read the full
  summary table (p-values, confidence intervals per coefficient) rather than
  just sklearn's point estimates.
- Cross-validate the Ridge/Lasso alpha instead of picking one by hand.

## What I found

_(fill in after you finish)_
