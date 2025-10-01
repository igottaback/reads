from flask import Flask, request, jsonify

app = Flask(__name__)
latest_data = {}

@app.route('/update', methods=['POST'])
def update():
    global latest_data
    latest_data = request.json
    return jsonify({"status": "received"}), 200

@app.route('/get', methods=['GET'])
def get_data():
    return jsonify(latest_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
