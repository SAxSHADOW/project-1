from transformers import pipeline

# Load pre-trained emotion model
emotion_model = pipeline("text-classification", 
                         model="bhadresh-savani/bert-base-uncased-emotion")

def analyze_text(text):
    result = emotion_model(text)
    emotion = result[0]['label'].lower()
    return emotion

def predict_risk(emotion):
    if emotion is ["sadness", "anxiety", "depression"]:
        return "High Risk"
    elif emotion is ["anger","fear"]:
        return "Medium Risk"
    elif emotion is ["sadness"]:
        return "Low Risk"
    else:
        return "No Risk"

def Mental_State(emotion):
    if emotion is ["sadness", "anxiety", "depression"]:
        return "Signs of Depression"
    elif emotion is ["anger","fear"]:
        return "Signs of Anxiety"
    elif emotion is ["sadness"]:
        return "Signs of Stress"
    else:
        return "Normal"