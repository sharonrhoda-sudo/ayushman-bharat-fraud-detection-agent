import streamlit as st
from src.ingestion import load_claims
from src.feature_engineering import create_features
from src.anomaly_model import train_model, predict
from src.rules_engine import apply_rules
from src.risk_scoring import calculate_risk
from src.config import FEATURES

def show():
    st.title("🔍 Fraud Analysis")

    try:
        df = load_claims()
        st.info(f"Loaded {len(df)} claims")
    except FileNotFoundError:
        st.warning("Claims CSV not found. Upload data first.")
        return

    df_features = create_features(df)

    st.subheader("Train & Predict Fraud")
    if st.button("Run Analysis"):
        # ✅ Retrain model on new FEATURES
        model = train_model(df_features, FEATURES)
        st.success("Model trained successfully on new features!")

        # ✅ Predict
        df_pred = predict(model, df_features, FEATURES)

        # Apply rules and risk scoring
        df_rules = apply_rules(df_pred)
        df_risk = calculate_risk(df_rules)

        st.dataframe(df_risk.head(10))
        st.success("Fraud analysis complete!")