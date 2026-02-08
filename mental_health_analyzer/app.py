from flask import Flask, render_template, request
from emotion_model import analyze_text
from data_model import predict_risk_from_text
from chatbot import chatbot_reply

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    risk = None
    Mental_State = None
    bot_reply = None

    if request.method == "POST":
        text = request.form.get("text")

        if text:
            # Emotion detection
            emotion = analyze_text(text)
            result = emotion

            # ML-based risk prediction
            risk, Mental_State = predict_risk_from_text(emotion)

            # Chatbot response
            bot_reply = chatbot_reply(text)

    return render_template(
        "index.html",
        result=result,
        risk=risk,
        Mental_State=Mental_State,
        bot_reply=bot_reply
    )

if __name__ == "__main__":
    app.run(debug=True)
