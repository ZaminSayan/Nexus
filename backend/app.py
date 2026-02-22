from flask import Flask, request, jsonify
import subprocess
import datetime
import random
import os
import webbrowser

app = Flask(__name__)

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    user_input = data.get("command", "").lower().strip()

    # OPEN APPLICATIONS
    if "open brave" in user_input:
        subprocess.Popen(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
        return jsonify({"response": "Brave is ready. Explore wisely."})

    if "open notepad" in user_input:
        subprocess.Popen("notepad.exe")
        return jsonify({"response": "Notepad opened. Time to write history."})

    # TIME & DATE
    if "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return jsonify({"response": f"It is currently {current_time}."})

    if "date" in user_input:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return jsonify({"response": f"Today is {today}."})

    # CALCULATOR
    if user_input.startswith("calculate"):
        try:
            expression = user_input.replace("calculate", "").strip()
            result = eval(expression)
            return jsonify({"response": f"The answer is {result}."})
        except:
            return jsonify({"response": "That calculation confused me. Try again."})

    # SEARCH
    if user_input.startswith("search"):
        query = user_input.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return jsonify({"response": f"Searching for {query}."})

    # JOKE
    if "joke" in user_input:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why did the computer get cold? It forgot to close Windows.",
            "I would tell you a UDP joke... but you might not get it."
        ]
        return jsonify({"response": random.choice(jokes)})

    # GREETINGS
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return jsonify({"response": "Hello. I'm Nexus. What shall we build today?"})

    return jsonify({"response": "I am not sure how to respond to that yet."})