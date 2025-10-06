# server.py  (on Render)
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1421676240980414526/i8SJaZZc3z3_7Bw0XGehaWOkZlKK0hDin2QdCvKHSzRCmKG1IG53iyBrRroDfuc8rA_I"  # your real webhook
latest = {}  # store the most recent message

@app.route("/send-to-discord", methods=["POST"])
def send_to_discord():
    global latest
    data = request.json or {}
    latest = data  # save it so it can be read later

    # forward the same info to Discord
    msg = f"Pet: {data.get('pet')}\nPrice: {data.get('price')}\nJobID: {data.get('jobId')}"
    requests.post(WEBHOOK_URL, json={"content": msg})
    return {"status": "sent"}

@app.route("/latest", methods=["GET"])
def get_latest():
    return jsonify(latest or {"status": "no data"})

@app.route("/")
def ping():
    return ":check: API is working!"
