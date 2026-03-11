import joblib
from sklearn.ensemble import IsolationForest
import os

MODEL_PATH = "models/isolation_forest.pkl"

def train_model(df, features):
    """
    Train Isolation Forest on given features.
    """
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(df[features])
    
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    return model

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model not trained yet.")
    return joblib.load(MODEL_PATH)

def predict(model, df, features):
    """
    Predict anomalies. Features must match training features exactly.
    """
    # Ensure all features exist
    for f in features:
        if f not in df.columns:
            df[f] = 0  # default if missing
    
    preds = model.predict(df[features])
    df['anomaly'] = preds
    df['fraud_flag'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0)
    return df