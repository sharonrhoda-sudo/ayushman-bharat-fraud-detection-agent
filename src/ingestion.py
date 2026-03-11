import pandas as pd
import os

def load_claims(file_path="data/raw/claims.csv"):
    """
    Load insurance claims CSV file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Claims file not found at {file_path}")
    
    df = pd.read_csv(file_path)
    return df