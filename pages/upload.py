import streamlit as st
import pandas as pd
import os

def show():
    st.title("📁 Upload Claims Data")
    
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"Uploaded {len(df)} rows successfully!")
            st.dataframe(df.head(10))

            # Save to raw data folder
            os.makedirs("data/raw", exist_ok=True)
            df.to_csv("data/raw/claims.csv", index=False)
            st.info("Saved to data/raw/claims.csv")
        except Exception as e:
            st.error(f"Error uploading file: {e}")