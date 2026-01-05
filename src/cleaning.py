import pandas as pd

def clean_data(df):
    df = df.dropna(subset=["StudentID", "Test_Score"])
    df= df.drop_duplicates(subset=["StudentID"])
    df.columns = ( 
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        )
    df["Test_Score"] = pd.to_numeric(df["Test_Score"], errors="coerce")
    df["Hours_Studied"] = pd.to_numeric(df["Hours_Studied"], errors="coerce")
    
    df.loc[(df["Test_Score"] > 100) | (df["Test_Score"] < 0), "Test_Score"] = pd.NA
    df.loc[(df["Hours_Studied"] > 25), "Hours_Studied"] = pd.NA
    return df