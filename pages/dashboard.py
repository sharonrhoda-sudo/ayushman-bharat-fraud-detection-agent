import streamlit as st
from src.ingestion import load_claims
from src.feature_engineering import create_features
from src.anomaly_model import train_model, predict
from src.rules_engine import apply_rules
from src.risk_scoring import calculate_risk
from src.config import FEATURES
import os

def show():
    st.title("📊 Fraud Detection Dashboard")
    
    try:
        df = load_claims()
        st.success(f"Loaded {len(df)} claims successfully!")
    except FileNotFoundError:
        st.warning("Claims CSV not found. Upload data first.")
        return

    df_features = create_features(df)

    # ✅ Retrain model if it does not exist
    from src.anomaly_model import MODEL_PATH
    if not os.path.exists(MODEL_PATH):
        st.info("No trained model found. Training now...")
        model = train_model(df_features, FEATURES)
        st.success("Model trained successfully!")
    else:
        from src.anomaly_model import load_model
        model = load_model()
        st.info("Loaded existing model.")

    # Predict and compute risk
    df_pred = predict(model, df_features, FEATURES)
    df_rules = apply_rules(df_pred)
    df_risk = calculate_risk(df_rules)

    st.subheader("Fraud Risk Overview")
    risk_counts = df_risk['risk_category'].value_counts()
    st.bar_chart(risk_counts)