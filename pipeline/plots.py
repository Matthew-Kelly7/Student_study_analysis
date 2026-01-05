import os
import matplotlib.pyplot as plt
import seaborn as sns



def generate_plots(df, df_pass, df_fail, plots_folder="plots"):
    
    # Ensure plots folder exists
    if os.path.exists(plots_folder):
        if not os.path.isdir(plots_folder):
            os.remove(plots_folder)
        os.makedirs(plots_folder, exist_ok=True)
        
    sns.set_theme(style="whitegrid", context="talk")
    
    # Scatter: Hours Studied vs Test Score
    
    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="Hours_Studied",
        y="Test_Score",
        alpha=0.7,
        s=120)
    # Trend Line
    sns.regplot(
        data=df,
        x="Hours_Studied",
        y="Test_Score",
        scatter=False,
        color="black",
        line_kws={"linewidth": 2, "linestyle": "--"})
    plt.title("Relationship between hours studied and test score",
              fontsize=16, weight="bold")
    plt.xlabel("Hours studied", fontsize=12)
    plt.ylabel("Test score", fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(
        plots_folder, "Hours_studied_vs_test_score.png"), dpi=300)
    
    
    # Scatter: Attendance vs Test Score
    
    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="Attendance_Percent",
        y="Test_Score",
        alpha=0.7,
        s=120)
    # Trend Line
    sns.regplot(
        data=df,
        x="Attendance_Percent",
        y="Test_Score",
        scatter=False,
        color="black",
        line_kws={"linewidth": 2, "linestyle": "--"})
    plt.title("Relationship between Attendance Percentage and test score")
    plt.xlabel("Attendance percentage")
    plt.ylabel("Test Scores")
    plt.tight_layout()
    plt.savefig(os.path.join(
        plots_folder, "Attendance_vs_test_score.png"), dpi=300)

    # Bar chart: Pass vs Fail Count
    
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(
        x=["Pass", "Fail"],
        y=[len(df_pass), len(df_fail)])

    for p in ax.patches:
        height = p.get_height()
        ax.annotate(
            f"{int(height)}",
            (p.get_x() + p.get_width() / 2, height),
            ha="center",
            va="bottom",
            fontsize=12,
            fontweight="bold")
    plt.title("Pass vs Fail Distribution", fontsize=16, weight="bold")
    plt.ylabel("Number of Students", fontsize=12)
    plt.xlabel("")
    plt.tight_layout()

    plt.savefig(os.path.join(plots_folder, "Pass_vs_Fail.png"), dpi=300)
    plt.close()
    
    
    # Correlation heatmap
    
    correlation_matrix = df[["Hours_Studied","Attendance_Percent", "Test_Score"]].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correelation Matrix")
    plt.tight_layout()
    plt.savefig(os.path.join(
        plots_folder, "Correlation_Analysis_Heatmap.png"), dpi=300)