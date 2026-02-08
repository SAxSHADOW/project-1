def chatbot_reply(text):
    text = text.lower()

    if "sad" in text or "depressed" in text:
        return "I'm really sorry you're feeling this way. You're not alone."

    elif "stress" in text or "anxious" in text:
        return "Try taking a deep breath. Talking to someone may help."

    elif "happy" in text:
        return "That's wonderful to hear! Keep smiling 😊"

    else:
        return "Thank you for sharing. I'm here to listen."
