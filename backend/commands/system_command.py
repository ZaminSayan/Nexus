# backend/commands/system_command.py
import subprocess
import datetime
import random

def handle_time(command):
    if "time" in command.lower():
        return datetime.datetime.now().strftime("It is currently %I:%M %p.")
    return None

def handle_date(command):
    if "date" in command.lower():
        return datetime.datetime.now().strftime("Today is %A, %B %d, %Y.")
    return None

def handle_greeting(command):
    if any(word in command.lower() for word in ["hi", "hello", "hey"]):
        responses = [
            "Hello! I'm Nexus. What shall we do today?",
            "Hi there! Ready to build something cool?",
        ]
        return random.choice(responses)
    return None


def handle_system(command):
    for func in [handle_time, handle_date, handle_greeting]:
        result = func(command)
        if result:
            return result
    return None