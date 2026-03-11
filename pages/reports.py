import streamlit as st
from src.ingestion import load_claims
from src.feature_engineering import create_features
from src.anomaly_model import load_model, predict
from src.rules_engine import apply_rules
from src.risk_scoring import calculate_risk
from src.report_generator import generate_report
import os

def show():
    st.title("📄 Generate Fraud Reports")

    try:
        df = load_claims()
    except FileNotFoundError:
        st.warning("Claims CSV not found. Upload data first.")
        return

    df_features = create_features(df)

    try:
        model = load_model()
        df_pred = predict(model, df_features, ['claim_amount_log', 'num_procedures', 'hospital_id', 'patient_id'])
        df_rules = apply_rules(df_pred)
        df_risk = calculate_risk(df_rules)
    except FileNotFoundError:
        st.warning("Model not trained yet. Run Fraud Analysis first.")
        return

    st.subheader("Download Report")
    if st.button("Generate CSV Report"):
        report_path = "reports/fraud_report.csv"
        os.makedirs("reports", exist_ok=True)
        report = generate_report(df_risk, file_path=report_path)
        st.success(f"Report saved at {report_path}")
        st.download_button("Download Report CSV", data=open(report_path, "rb"), file_name="fraud_report.csv")