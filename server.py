# server.py (middleman)
from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1421676240980414526/i8SJaZZc3z3_7Bw0XGehaWOkZlKK0hDin2QdCvKHSzRCmKG1IG53iyBrRroDfuc8rA_I"

@app.route("/send-to-discord", methods=["POST"])
def send_to_discord():
    data = request.json
    msg = f"Player: {data['player']}\nPet: {data['pet']}\nValue: {data['value']}"
    requests.post(WEBHOOK_URL, json={"content": msg})
    return {"status": "sent"}

@app.route("/")
def ping():
    return ":check: API is working!"
