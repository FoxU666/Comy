from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "online", "message": "Comy AI Backend is running!"})

@app.route("/api/comy", methods=["POST"])
def comy_endpoint():
    data = request.json
    player_message = data.get("message", "").lower()
    
    # Prosta logika rozpoznawania poleceń dla Baritone
    response_action = ""
    if "chodź" in player_message or "chodz" in player_message:
        reply_text = "Okej, ruszam za Tobą!"
        response_action = "#follow"
    elif "kop" in player_message:
        reply_text = "Rozumiem, zaczynam kopanie."
        response_action = "#mine"
    else:
        reply_text = f"Odebrałem wiadomość: '{player_message}'."

    return jsonify({
        "reply": reply_text,
        "action": response_action
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
