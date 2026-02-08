import random

def chatbot_reply(text, emotion=None, risk=None):
    text = text.lower()

    # High-risk keywords
    danger_words = ["suicide", "kill myself", "end my life", "die", "worthless"]

    if any(word in text for word in danger_words):
        return (
            "I'm really sorry you're feeling this way. "
            "You are not alone. It might help to talk to someone you trust "
            "or a mental health professional."
        )

    # Emotion-based replies
    emotion_responses = {
        "joy": [
            "That's great to hear! What made you feel this way?",
            "It sounds like something positive is happening in your life.",
            "I'm glad you're feeling good today!"
        ],
        "sadness": [
            "I'm sorry you're feeling sad. Do you want to talk about it?",
            "That sounds difficult. I'm here to listen.",
            "It's okay to feel this way sometimes."
        ],
        "anger": [
            "It sounds like something frustrated you.",
            "Would you like to share what made you feel angry?",
            "Taking a deep breath might help in moments like this."
        ],
        "fear": [
            "That sounds worrying. What is making you feel this way?",
            "You're safe here. Do you want to talk more about it?",
            "Sometimes sharing fears makes them easier to handle."
        ],
        "neutral": [
            "I see. Would you like to share more?",
            "I'm here to listen whenever you're ready.",
            "Tell me more about how you're feeling."
        ]
    }

    # Default fallback
    default_responses = [
        "I'm here to listen. Tell me more.",
        "How long have you been feeling this way?",
        "Would you like to talk more about it?"
    ]

    if emotion in emotion_responses:
        return random.choice(emotion_responses[emotion])

    return random.choice(default_responses)
