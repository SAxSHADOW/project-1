def analyze_text(text):
    text = text.lower()

    if any(word in text for word in ["sad", "depressed", "hopeless"]):
        return "sadness"
    elif any(word in text for word in ["happy", "excited", "great"]):
        return "joy"
    elif any(word in text for word in ["angry", "mad", "frustrated"]):
        return "anger"
    elif any(word in text for word in ["scared", "afraid", "anxious"]):
        return "fear"
    else:
        return "neutral"
