# DS / ML Skills — Learn by Doing

A personal practice repo: one folder per skill, each with a self-contained project.
The goal isn't to collect finished solutions — it's to rebuild fluency by doing the
work. Every `analysis.py` is a **skeleton**: imports and data are wired up, the
steps are laid out as `TODO`s, and you fill in the modeling/analysis logic yourself.

## Structure

Each skill folder follows the same pattern:

```
skill-name/
  README.md          — what the skill is, the scenario, the tasks, stretch goals
  generate_data.py    — creates synthetic data in data/ (or notes on a real dataset)
  analysis.py          — starter script with TODOs; this is where you do the work
  data/                — generated/downloaded data lands here (gitignored)
  notebooks/            — optional space for exploratory notebooks
```

## Skills covered (so far)

| Folder | Skill |
|---|---|
| [`hypothesis-testing-ab-testing/`](hypothesis-testing-ab-testing/) | Hypothesis testing, A/B testing, power analysis |
| [`causal-inference/`](causal-inference/) | Confounding, regression adjustment, propensity scores, diff-in-diff |
| [`linear-regression/`](linear-regression/) | OLS, regularization, diagnostics |
| [`logistic-regression/`](logistic-regression/) | Classification, class imbalance, ROC/AUC, odds ratios |
| [`clustering/`](clustering/) | K-means, hierarchical clustering, segmentation |
| [`dimensionality-reduction/`](dimensionality-reduction/) | PCA, variance explained, visualization |
| [`marketing-mix-modeling/`](marketing-mix-modeling/) | Adstock, saturation curves, channel ROI |
| [`uplift-incrementality/`](uplift-incrementality/) | Heterogeneous treatment effects, T-learner/S-learner, Qini curves |

More can be added the same way — new folder, same four pieces.

## Setup

```bash
cd /Users/f/ds-ml-skills
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Workflow per skill

1. Read that folder's `README.md` for the scenario and objective.
2. Run `python generate_data.py` to produce the dataset in `data/`.
3. Open `analysis.py`, work through the `TODO`s top to bottom.
4. Use `notebooks/` for scratch exploration if you prefer notebooks to scripts.
5. Once done, write a short "what I found" summary at the bottom of the README —
   that's the part that will actually stick, and it's material you can reuse in
   interviews or a portfolio later.
