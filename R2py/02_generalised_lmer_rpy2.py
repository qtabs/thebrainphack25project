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


def main():
    # ---- Example usage ----
    df = pd.DataFrame({
        "depVar": [1.2, 2.0, 1.5, 2.5, 1.1, 2.2],
        "fixed1": [0, 1, 0, 1, 0, 1],
        "subject": [1, 1, 2, 2, 3, 3]
    })

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
