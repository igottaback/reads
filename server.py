from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store (will reset when server restarts)
latest_data = {}

@app.route("/")
def index():
    return "✅ API is working!"

@app.route("/send-data", methods=["POST"])
def receive_data():
    data = request.json
    if not data:
        return jsonify({"error": "Missing JSON"}), 400
    
    # Save data globally
    global latest_data
    latest_data = data

    return jsonify({"status": "✅ Received", "data": data})

@app.route("/get-data", methods=["GET"])
def get_data():
    global latest_data
    return jsonify(latest_data)
