import pandas as pd

# Split by Threshold
def split_by_threshold(df, threshold):
    df_pass = df[df["Test_Score"] >= threshold]
    df_fail = df[df["Test_Score"] < threshold]
    pass_count = len(df_pass)
    fail_count = len(df_fail)
    print("Pass:", pass_count)
    print("Fail:", fail_count)
    return df_pass, df_fail

# Creating Pass/Fail Column
def add_results_column(df, threshold):
    df["Pass/Fail"] = df["Test_Score"].apply(
        lambda x: "Pass" if x >= threshold else "Fail")
    return df

# Create student grades column
def create_grades_column(df):
    df["Grade"] = df["Test_Score"].map(
        lambda x: "A" if x >= 85
        else "B" if x >= 70
        else "C" if x >= 60
        else "D")
    return df