from transformers import pipeline

# Load pre-trained emotion model
emotion_model = pipeline(
    "text-classification", model="bhadresh-savani/bert-base-uncased-emotion"
)

def analyze_text(text):
    if not text or not text.strip():
        return "No Emotion"

    lowered = text.lower()
    # If there are no alphabetic characters or text is too short, treat as no emotion.
    letters_only = "".join(ch for ch in lowered if ch.isalpha() or ch.isspace())
    words = [w for w in letters_only.split() if len(w) >= 3]
    if len(words) == 0:
        return "No Emotion"
    # Keyword override for explicit mental-health terms not in the model's labels.
    if "depress" in lowered:
        return "depression"

    result = emotion_model(text)
    if not result:
        return "No Emotion"
    top = result[0]
    emotion = top["label"].lower()
    score = float(top.get("score", 0))
    # Low confidence -> treat as no emotion.
    if score < 0.6:
        return "No Emotion"
    if emotion not in MENTAL_STATE_MAP and emotion not in RISK_MAP:
        return "No Emotion"
    return emotion

# Map model emotions to a simplified mental state and risk level.
# Model labels are: sadness, joy, love, anger, fear, surprise.
MENTAL_STATE_MAP = {
    "sadness": "Signs of Sadness",
    "fear": "Signs of Anxiety",
    "depression": "Signs of Depression",
    "anger": "Signs of Stress",
}

RISK_MAP = {
    "sadness": "Low Risk",
    "fear": "Medium Risk",
    "anger": "High Risk",
    "depression": "High Risk",
}

def predict_risk(emotion):
    return RISK_MAP.get(emotion, "No Risk")

def Mental_State(emotion):
    return MENTAL_STATE_MAP.get(emotion, "Normal")
