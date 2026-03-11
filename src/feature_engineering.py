import pandas as pd
import numpy as np
from .config import FEATURES

def create_features(df):
    """
    Create features for fraud detection. Robust to missing columns.
    """
    df = df.copy()
    
    # claim_amount_log
    if 'claim_amount' in df.columns:
        df['claim_amount_log'] = df['claim_amount'].apply(lambda x: 0 if pd.isna(x) or x <= 0 else np.log(x))
    else:
        df['claim_amount_log'] = 0

    # num_procedures
    if 'procedure_codes' in df.columns:
        df['num_procedures'] = df['procedure_codes'].apply(lambda x: len(str(x).split(',')))
    else:
        df['num_procedures'] = 0

    # hospital_id encoding
    if 'hospital_id' in df.columns:
        df['hospital_id'] = df['hospital_id'].astype('category').cat.codes
    else:
        df['hospital_id'] = 0

    # patient_id encoding
    if 'patient_id' in df.columns:
        df['patient_id'] = df['patient_id'].astype('category').cat.codes
    else:
        df['patient_id'] = 0

    return df