"""
Generalized mixed-effects modeling with pymer4

This script demonstrates:
- Using pandas DataFrame as input
- Fitting linear mixed-effects models (LMM) with pymer4
- Dynamically specifying dependent variable, fixed effects, and random effects
- Printing model summary and ANOVA

Dependencies:
    pip install pandas pymer4
R packages required (installed automatically by pymer4 if needed):
    lme4, lmerTest
"""

import pandas as pd
from pymer4.models import lmer


def run_mixed_model_pymer4(df: pd.DataFrame, dep_var: str, fixed_effects: list, random_effects: list):
    """
    Fit a linear mixed-effects model using pymer4.

    Parameters
    ----------
    df : pd.DataFrame
        The dataset.
    dep_var : str
        Name of the dependent variable column.
    fixed_effects : list of str
        List of fixed-effect predictor columns.
    random_effects : list of str
        List of random-effect grouping variables.

    Returns
    -------
    model : pymer4 Lmer object
        The fitted model object with summary and ANOVA available.
    """

    # ---- Build the formula ----
    fixed_str = " + ".join(fixed_effects) if fixed_effects else "1"
    random_str = " + ".join([f"(1|{v})" for v in random_effects]) if random_effects else ""
    formula = f"{dep_var} ~ {fixed_str}"
    if random_str:
        formula += " + " + random_str

    # ---- Fit the model ----
    model = lmer(formula, data=df)
    model.fit(factors=None, summarize=False)  # factors=None leaves categorical handling to pymer4

    return model


def main():
    # ---- Example DataFrame ----
    df = pd.DataFrame({
        "depVar": [1.2, 2.0, 1.5, 2.5, 1.1, 2.2],
        "fixed1": [0, 1, 0, 1, 0, 1],
        "subject": [1, 1, 2, 2, 3, 3]
    })

    dep_var = "depVar"
    fixed_effects = ["fixed1"]
    random_effects = ["subject"]

    # ---- Run the generalized mixed-effects model ----
    model = run_mixed_model_pymer4(df, dep_var, fixed_effects, random_effects)

    # ---- Print results ----
    print("\n=== Model Summary ===")
    print(model.summary())

    print("\n=== ANOVA Table ===")
    print(model.anova())


if __name__ == "__main__":
    main()
