# backend/commands/utility_command.py
import subprocess   
import webbrowser
import random

def handle_calculate(command):
    if command.lower().startswith("calculate"):
        try:
            expr = command.lower().replace("calculate", "").strip()
            result = eval(expr)
            return f"The answer is {result}."
        except:
            return "That calculation confused me. Try again."
    return None

def handle_search(command):
    if command.lower().startswith("search"):
        query = command.lower().replace("search", "").strip()
        # Open specifically in Brave
        brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        subprocess.Popen([brave_path, f"https://www.google.com/search?q={query}"])
        return f"Searching for {query} in Brave."
    return None
def handle_joke(command):
    if "joke" in command.lower():
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why did the computer get cold? It forgot to close Windows.",
            "I would tell you a UDP joke... but you might not get it."
        ]
        return random.choice(jokes)
    return None


def handle_utility(command):
    for func in [handle_calculate, handle_search, handle_joke]:
        result = func(command)
        if result:
            return result
    return None