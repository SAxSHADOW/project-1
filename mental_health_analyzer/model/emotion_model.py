from transformers import pipeline

# Load pre-trained emotion model
emotion_model = pipeline("text-classification", 
                         model="bhadresh-savani/bert-base-uncased-emotion")

def analyze_text(text):
    result = emotion_model(text)
    emotion = result[0]['label']
    return emotion

def predict_risk(Feeling):
    if Feeling in ["sadness", "anxiety", "Depression"]:
        return "High Risk"
    elif Feeling in ["anger","fear"]:
        return "Medium Risk"
    elif Feeling in ["sadness"]:
        return "Low Risk"
    else:
        return "No Risk"

def Mental_State(Emotion):
    if Emotion in ["sadness", "anxiety", "Depression"]:
        return "Signs of Depression"
    elif Emotion in ["anger","fear"]:
        return "Signs of Anxiety"
    elif Emotion in ["sadness"]:
        return "Signs of Sadness"
    else:
        return "Normal"