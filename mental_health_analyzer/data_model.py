import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET = os.path.join(BASE_DIR, "dataset/final_mental_health_dataset.csv")
MODEL_FILE = "risk_model.pkl"


def train_model():
    df = pd.read_csv(DATASET)

    features = [
        "Gender",
        "family_history",
        "treatment",
        "Growing_Stress",
        "Mood_Swings",
        "Coping_Struggles",
        "Work_Interest",
        "Social_Weakness"
    ]

    df = df.dropna(subset=["Mental_Health_Risk"])
    df[features] = df[features].fillna("unknown")

    X = df[features].astype(str)
    y = df["Mental_Health_Risk"].astype(str)

    encoders = {}
    X_encoded = pd.DataFrame()

    for col in X.columns:
        le = LabelEncoder()
        X_encoded[col] = le.fit_transform(X[col])
        encoders[col] = le

    target_le = LabelEncoder()
    y_encoded = target_le.fit_transform(y)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_encoded, y_encoded)

    joblib.dump((model, encoders, target_le), MODEL_FILE)


def load_model():
    if not os.path.exists(MODEL_FILE):
        train_model()
    return joblib.load(MODEL_FILE)


def predict_risk_from_text(emotion, text=None):
    text = text.lower() if text else ""

    high_risk_words = ["suicide", "die", "kill", "worthless", "hopeless"]
    medium_risk_words = ["tired", "alone", "sad", "stressed", "depressed"]

    if any(word in text for word in high_risk_words):
        return "High", "Critical"

    if any(word in text for word in medium_risk_words):
        return "Medium", "Struggling"

    if emotion in ["sadness", "fear"]:
        return "Medium", "Needs Support"

    if emotion == "joy":
        return "Low", "Positive"

    return "Low", "Stable"
