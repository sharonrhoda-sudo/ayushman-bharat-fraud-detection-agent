def calculate_risk(df):
    """
    Combine model prediction and rules to calculate risk score.
    """
    df = df.copy()
    df['risk_score'] = df['fraud_flag']*0.7 + df['rule_flag']*0.3
    df['risk_category'] = df['risk_score'].apply(lambda x: "High" if x > 0.5 else "Low")
    return df