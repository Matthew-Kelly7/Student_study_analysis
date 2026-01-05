from file_io import load_data
from cleaning import clean_data
from analysis import split_by_threshold, create_grades_column, add_results_column
from plot_utils import generate_plots 
from reporting import auto_report

DATA_PATH = "data/raw"
OUTPUT = "data/processed"
threshold = 60


def main():
    os.makedirs(OUTPUT, exist_ok = True)
    df = load_data(DATA_PATH)
    df = clean_data(df)
    df_pass, df_fail = split_by_threshold(df, threshold)
    df = create_grades_column(df, threshold)
    df = add_results_column(df)

    df.to_csv(f"{OUTPUT}/students_clean.csv", index=False)
    df_pass.to_csv(f"{OUTPUT}/passed_students.csv", index=False)
    df_fail.to_csv(f"{OUTPUT}/failed_students.csv", index=False)

    generate_plots(df, df_pass, df_fail)
    print("Plots Generated")

    auto_report(df, df_pass, df_fail)
    print("Report generated")

    print("Pipeline ran successfully")
    print(df.head())
    print(df.isna().sum())



if __name__ == "__main__":
    main()