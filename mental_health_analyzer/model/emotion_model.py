from transformers import pipeline

# Load pre-trained emotion model
emotion_model = pipeline("text-classification", 
                         model="bhadresh-savani/bert-base-uncased-emotion")

def analyze_text(text):
    result = emotion_model(text)
    emotion = result[0]['label']
    return emotion

def predict_risk(emotion):
    if emotion in ["sadness", "fear"]:
        return "High Risk"
    elif emotion in ["anger"]:
        return "Medium Risk"
    else:
        return "Low Risk"