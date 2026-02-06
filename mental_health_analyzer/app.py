from flask import Flask, render_template, request
from model.emotion_model import analyze_text, predict_risk
from chatbot.chatbot import chatbot_reply

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    risk = None
    bot_reply = None

    if request.method == "POST":
        text = request.form["text"]

        # AI Emotion Analysis
        emotion = analyze_text(text)

        # Risk Prediction
        risk = predict_risk(Feelings)

        #Mental_State
        Mental_State = Mental_State(Emotion)

        # Chatbot Response
        bot_reply = chatbot_reply(text)

        result = emotion

    return render_template("index.html", result=result, risk=risk, Mental_State=Mental_State, bot_reply=bot_reply)

if __name__ == "__main__":
    app.run(debug=True)
