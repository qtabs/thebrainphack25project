"""
Generalized mixed-effects model runner (lme4/lmerTest) from pandas DataFrame using rpy2.

Dependencies:
    pip install pandas rpy2
R packages required:
    install.packages("lme4")
    install.packages("lmerTest")
"""

import pandas as pd
from rpy2.robjects import r, globalenv
from rpy2.robjects.packages import importr
from rpy2.robjects.conversion import localconverter
from rpy2.robjects import pandas2ri


def run_mixed_model(
    df: pd.DataFrame,
    dep_var: str,
    fixed_effects: list,
    random_effects: list,
    use_lmerTest: bool = False
):
    """
    Fits a linear mixed-effects model using lme4 or lmerTest.

    Parameters
    ----------
    df : pd.DataFrame
        The data.
    dep_var : str
        Dependent variable name.
    fixed_effects : list of str
        Names of fixed effect predictors.
    random_effects : list of str
        Names of random effect grouping variables.
    use_lmerTest : bool
        Whether to use lmerTest (adds Type III ANOVA).

    Returns
    -------
    model_summary, anova_table : R objects
        The summary and ANOVA table of the fitted model.
    """

    # ---- Import R packages ----
    base = importr("base")
    stats = importr("stats")
    lme4 = importr("lme4")
    if use_lmerTest:
        lmerTest = importr("lmerTest")

    # ---- Convert pandas DataFrame -> R data.frame ----
    with localconverter(pandas2ri.converter):
        r_df = pandas2ri.py2rpy(df)
    globalenv["dd"] = r_df  # assign to R global environment

    # ---- Build lmer formula ----
    fixed_str = " + ".join(fixed_effects) if fixed_effects else "1"
    random_str = " + ".join([f"(1 | {v})" for v in random_effects]) if random_effects else ""
    formula_str = f"{dep_var} ~ {fixed_str}"
    if random_str:
        formula_str += " + " + random_str

    # ---- Fit the model ----
    if use_lmerTest:
        model = lmerTest.lmer(formula_str, data=r_df)
    else:
        model = lme4.lmer(formula_str, data=r_df)

    # ---- Return summary and ANOVA ----
    model_summary = base.summary(model)
    anova_table = stats.anova(model)
    return model_summary, anova_table
import numpy as np
import pandas as pd
from numpy import random
import math


def generate_dataframe(
    n_samples,
    n_subjects,
    sigma_observation,
    beta_variability,
    intercept_variability,
    beta_group,
    intercept_group,
):
    """
    Generate a long-format dataframe for a mixed-effects simulation.

    Each subject has its own slope (beta_subject) and intercept (k_subject),
    drawn from normal distributions around group means.

    Returns a dataframe with columns:
        subject, x, y
    """

    records = []  # list of rows to build long dataframe

    for s in range(1, n_subjects + 1):

        # subject-level slope and intercept
        beta_subject = random.normal(loc=beta_group, scale=beta_variability)
        k_subject = random.normal(loc=intercept_group, scale=intercept_variability)

        # x for all samples of this subject
        x_vals = random.random(n_samples)

        # observation noise for each sample
        noise_vals = random.normal(loc=0, scale=sigma_observation, size=n_samples)

        # linear model
        y_vals = beta_subject * x_vals + k_subject + noise_vals

        # append each row
        for i in range(n_samples):
            records.append([s, y_vals[i], x_vals[i]])

    df = pd.DataFrame(records, columns=["subject",  "depVar","fixed1"])
    return df





def main():
        
    # -----------------------------
    # Example Usage
    # -----------------------------
    n_samples = 10
    n_subjects = 10

    sigma_observation = 1 / math.sqrt(2)
    beta_variability = 1
    intercept_variability = 1 / math.sqrt(2)

    beta_group = 0
    intercept_group = 0

    df = generate_dataframe(
        n_samples=n_samples,
        n_subjects=n_subjects,
        sigma_observation=sigma_observation,
        beta_variability=beta_variability,
        intercept_variability=intercept_variability,
        beta_group=beta_group,
        intercept_group=intercept_group,
    )

    # Define model variables
    dep_var = "depVar"
    fixed_effects = ["fixed1"]
    random_effects = ["subject"]
    use_lmerTest = True

    summary, anova = run_mixed_model(df, dep_var, fixed_effects, random_effects, use_lmerTest)

    print("\n=== Model Summary ===")
    print(summary)
    print("\n=== ANOVA Table ===")
    print(anova)



if __name__ == "__main__":
    main()
