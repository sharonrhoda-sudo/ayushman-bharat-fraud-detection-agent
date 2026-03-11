import pandas as pd

def generate_report(df, file_path="reports/fraud_report.csv"):
    """
    Generate a CSV report for fraud detection.
    """
    import os
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    report = df[['claim_id', 'patient_id', 'hospital_id', 'claim_amount', 'fraud_flag', 'risk_score', 'risk_category']]
    report.to_csv(file_path, index=False)
    return report