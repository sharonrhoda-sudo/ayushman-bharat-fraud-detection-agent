def apply_rules(df):
    """
    Apply rule-based fraud checks.
    """
    df = df.copy()
    
    # Example rules
    df['rule_high_amount'] = df['claim_amount'].apply(lambda x: 1 if x > 100000 else 0)
    df['rule_many_procedures'] = df['num_procedures'].apply(lambda x: 1 if x > 5 else 0)
    
    # Combine rule flags
    df['rule_flag'] = df[['rule_high_amount', 'rule_many_procedures']].max(axis=1)
    
    return df