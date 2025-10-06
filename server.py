# server.py on Render
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1421676240980414526/i8SJaZZc3z3_7Bw0XGehaWOkZlKK0hDin2QdCvKHSzRCmKG1IG53iyBrRroDfuc8rA_I"
latest = {}

@app.route("/send-to-discord", methods=["POST"])
def send_to_discord():
    data = request.json
    # Save it so other clients can read it later
    global latest
    latest = data

    # Forward to Discord webhook
    requests.post(WEBHOOK_URL, json={"content": str(data)})
    return {"status": "sent"}

@app.route("/latest", methods=["GET"])
def get_latest():
    return jsonify(latest or {"status":"no data"})
