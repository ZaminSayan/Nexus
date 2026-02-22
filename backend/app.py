# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import random

# import command modules
from commands.open_command import handle_open
from commands.system_command import handle_system
from commands.utility_command import handle_utility

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "running"})

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    user_input = data.get("command", "").lower().strip()

    # try open commands
    result = handle_open(user_input)
    if result: return jsonify({"response": result})

    # try system commands (time/date/calc)
    result = handle_system(user_input)
    if result: return jsonify({"response": result})

    # try utility commands (search/joke)
    result = handle_utility(user_input)
    if result: return jsonify({"response": result})

    # fallback
    return jsonify({"response": "I am not sure how to respond to that yet."})

if __name__ == "__main__":
    print("Starting Nexus backend on http://localhost:5000")
    app.run(port=5000)