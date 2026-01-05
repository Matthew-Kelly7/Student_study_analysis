import os
import pandas as pd
import file_io
import datetime

def auto_report(df,df_pass,df_fail,report_folder="/Users/matthewkelly/spyder_code/Student_Project/reports"):
   
    # Ensure report folder exists
    if os.path.exists(report_folder):
        if not os.path.isdir(report_folder):
            os.remove(report_folder)  # remove if accidentally a file
    os.makedirs(report_folder, exist_ok=True)
    
    # Timestamped report filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(report_folder, f"automated_report_{timestamp}.txt")
    
    # Compute counts
    pass_count = len(df_pass)
    fail_count = len(df_fail)
    total = len(df)
    
    # Compute percentage of passes
    perc_passes = (pass_count/total)*100
    
    # Correlation
    correlation_matrix = df[["Hours_Studied", "Attendance_Percent", "Test_Score"]].corr()
    top_corr_value = correlation_matrix["Test_Score"].drop("Test_Score").max()
    top_corr_feature = correlation_matrix["Test_Score"].drop("Test_Score").idxmax()
    
    # Pivot table
    pivot=df.pivot_table(
        values=["Test_Score", "Hours_Studied"],
        index="Pass/Fail",
        aggfunc=["mean", "max", "min"])
    
    # Write report
    with open(report_file, "w") as f:
        
        f.write("=== AUTOMATED STUDENT REPORT ===\n\n")
        f.write("Data Summary:\n")
        f.write(df.describe().to_string())
        f.write("\n\nFirst 5 rows:\n")
        f.write(df.head().to_string()) 
        f.write(f"\nPass count: {pass_count}\n")
        f.write(f"Fail count: {fail_count}\n")
        f.write(f"Percentage of Passes: {perc_passes:.2f}%\n")
        f.write(f"Feature most correlated with Test_Score: {top_corr_feature} ({top_corr_value:.2f})\n")
        f.write("\nPivot Table (Test_Score & Hours_Studied by Pass_Fail):\n")
        f.write(pivot.to_string())
    