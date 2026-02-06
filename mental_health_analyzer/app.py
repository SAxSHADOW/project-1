from flask import Flask, render_template, request
from model.emotion_model import analyze_text, predict_risk, Mental_State
from chatbot.chatbot import chatbot_reply

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    risk = None
    Mental_State_value = None
    bot_reply = None

    if request.method == "POST":
        print("✅ POST request received")

        text = request.form.get("text")
        print("📝 User text:", text)

        if text:
            emotion = analyze_text(text)
            print("🎭 Emotion:", emotion)

        # AI Emotion Analysis
        emotion = analyze_text(text)
        result = emotion

        # Risk Prediction
        risk = predict_risk(emotion)

        #Mental_State
        Mental_State_value= Mental_State(emotion)

        # Chatbot Response
        bot_reply = chatbot_reply(text)

        result = emotion

    return render_template("index.html", result=result, risk=risk, Mental_State=Mental_State_value, bot_reply=bot_reply)

if __name__ == "__main__":
    app.run(debug=True)
