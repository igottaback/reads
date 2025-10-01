import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_URL = os.environ.get("https://discord.com/api/webhooks/1421676240980414526/i8SJaZZc3z3_7Bw0XGehaWOkZlKK0hDin2QdCvKHSzRCmKG1IG53iyBrRroDfuc8rA_I", "").strip()
BOT_TOKEN   = os.environ.get("MTQyMzA3MTk5MDY0MTg1MjQ5Ng.GyLEv1.jrqbzXMnaSj1NwKTqTP-MAi1Bfxspnm9wfBDY4", "").strip()
CHANNEL_ID  = os.environ.get("1421676230708691084", "").strip()
AUTH_KEY    = os.environ.get("sappisgay12!?", "").strip()

def require_auth():
    if request.headers.get("X-Auth-Key") != AUTH_KEY:
        return jsonify({"ok": False, "error": "unauthorized"}), 401
    return None

@app.route("/")
def ping():
    return ":check: API is working!"

@app.route("/send-to-discord", methods=["POST"])
def send_to_discord():
    auth = require_auth()
    if auth: return auth

    data = request.json or {}
    msg = f"Player: {data.get('player')}\nPet: {data.get('pet')}\nValue: {str(data.get('value'))}"
    r = requests.post(WEBHOOK_URL, json={"content": msg}, timeout=10)
    return {"ok": r.ok, "status": r.status_code}

@app.route("/recent", methods=["GET"])
def recent_messages():
    auth = require_auth()
    if auth: return auth

    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
    headers = {"Authorization": f"Bot {BOT_TOKEN}"}
    r = requests.get(url, headers=headers, params={"limit": 5}, timeout=10)

    if not r.ok:
        return {"ok": False, "status": r.status_code, "body": r.text}, 502

    msgs = []
    for m in r.json():
        msgs.append({
            "id": m["id"],
            "content": m["content"],
            "author": m["author"]["username"],
            "timestamp": m["timestamp"]
        })
    return {"ok": True, "messages": msgs}
