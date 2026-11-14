from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "online", "message": "Comy AI Backend is running!"})

@app.route("/api/comy", methods=["POST"])
def comy_endpoint():
    data = request.json
    # Tutaj w przyszłości dodasz logikę AI dla swojego moda
    player_action = data.get("action", "unknown")
    
    response_data = {
        "reply": f"Comy odebrało akcję: {player_action}. Wszystko działa poprawnie!"
    }
    return jsonify(response_data)

if __name__ == "__main__":
    # Render automatycznie przypisuje port przez zmienną środowiskową PORT
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
