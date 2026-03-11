import streamlit as st
from pages import dashboard, upload, analysis, reports

st.set_page_config(
    page_title="Fraud Detection Agent",
    layout="wide"
)

with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.title("🏥 Ayushman Bharat Fraud Detection Agent")

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Upload Data", "Fraud Analysis", "Reports"]
)

if menu == "Dashboard":
    dashboard.show()

elif menu == "Upload Data":
    upload.show()

elif menu == "Fraud Analysis":
    analysis.show()

elif menu == "Reports":
    reports.show()