import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Get absolute path to dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET = os.path.join(BASE_DIR, "dataset/Mental_Health_Dataset_modified.csv.csv")
MODEL_FILE = "treatment_model.pkl"


def train_model():
    df = pd.read_csv(DATASET)

    features = [
        "Gender",
        "Occupation",
        "self_employed",
        "family_history",
        "Days_Indoors",
        "Growing_Stress",
        "Changes_Habits",
        "Mental_Health_History",
        "Mood_Swings",
        "Coping_Struggles",
        "Work_Interest",
        "Social_Weakness",
        "mental_health_interview",
    ]

    df = df.dropna(subset=["treatment"])
    df[features] = df[features].fillna("unknown")

    X = df[features].astype(str)
    y = df["treatment"].astype(str)

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


def predict_treatment(input_dict):
    model, encoders, target_le = load_model()

    feature_order = [
        "Gender",
        "Occupation",
        "self_employed",
        "family_history",
        "Days_Indoors",
        "Growing_Stress",
        "Changes_Habits",
        "Mental_Health_History",
        "Mood_Swings",
        "Coping_Struggles",
        "Work_Interest",
        "Social_Weakness",
        "mental_health_interview",
    ]

    row = []
    for f in feature_order:
        val = str(input_dict.get(f, "unknown"))
        le = encoders[f]
        try:
            encoded = le.transform([val])[0]
        except:
            encoded = 0
        row.append(encoded)

    pred = model.predict([row])[0]
    return target_le.inverse_transform([pred])[0]


def predict_risk_from_text(emotion, text=None):
    text = text.lower() if text else ""

    high_risk_words = ["suicide", "die", "kill", "worthless", "hopeless"]
    medium_risk_words = ["tired", "alone", "sad", "stressed", "depressed"]

    # Keyword-based risk
    if any(word in text for word in high_risk_words):
        return "High", "Critical"

    if any(word in text for word in medium_risk_words):
        return "Medium", "Struggling"

    # Emotion-based fallback
    if emotion in ["sadness", "fear"]:
        return "Medium", "Needs Support"

    if emotion == "anger":
        return "Low", "Emotionally Active"

    if emotion == "joy":
        return "Low", "Positive"

    return "Low", "Stable"


    treatment = predict_treatment(input_dict)

    if treatment.lower() == "yes":
        return "High", "Needs Professional Support"
    else:
        return "Low", "Stable"
