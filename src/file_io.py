import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(
        path,
        na_values=["", "-", "missing", "NA"]
        )
        return df
    except:
        print("There was an error when loading data")