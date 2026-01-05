import streamlit as st
import pandas as pd
import plotly.express as px
import os


# Path to processed data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder where this script lives
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "processed", "students_clean.csv")

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

df = load_data(DATA_PATH)

# --- Ensure numeric types ---
df[["Test_Score", "Hours_Studied", "Attendance_Percent"]] = df[["Test_Score", "Hours_Studied", "Attendance_Percent"]].apply(pd.to_numeric)


st.title("Student Study Behaviour Dashboard")

# Key Metrics KPI

avg_study_time = df["Hours_Studied"].mean()
avg_attendance = df["Attendance_Percent"].mean()
avg_test_score = df["Test_Score"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("AVG Study Time (hrs)", f"{avg_study_time:.1f}")
col2.metric("AVG Attendance (%)", f"{avg_attendance:.1f}")
col3.metric("AVG Test Score", f"{avg_test_score:.1f}")

st.markdown("---")

# Study Time vs Test Score
fig1 = px.scatter(
    df,
    x="Hours_Studied",
    y="Test_Score",
    title="Hours Studied vs Test Score"
)
st.plotly_chart(fig1, use_container_width=True)

# Attendance vs Test Score
fig2 = px.scatter(
    df,
    x="Attendance_Percent",
    y="Test_Score",
    title="Attendance vs Test Score"
)
st.plotly_chart(fig2, use_container_width=True)

# Correlation Heatmap
corr = df[["Test_Score", "Hours_Studied", "Attendance_Percent"]].corr()
fig3 = px.imshow(
    corr,
    text_auto=True,
    title="Correlation between Study Factors and Test Score"
)
st.plotly_chart(fig3, use_container_width=True)



