import subprocess
import webbrowser
import random

# Map friendly names to URLs
SITE_MAP = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://www.github.com",
    "gmail": "https://mail.google.com",
    "stackoverflow": "https://stackoverflow.com",
    "chatgpt":"https://chatgpt.com",
    # add more sites here
}

def handle_open(command):
    """
    Handles opening apps or common websites.
    """
    cmd = command.lower().strip()

    # Specific apps
    if "open brave" in cmd:
        subprocess.Popen(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
        return "Brave is ready. Explore wisely."

    if "open notepad" in cmd:
        subprocess.Popen("notepad.exe")
        return "Notepad opened. Time to write history."

    # Friendly site names
    if cmd.startswith("open "):
        site = cmd.replace("open ", "").strip()
        url = SITE_MAP.get(site)
        if url:
            brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            subprocess.Popen([brave_path, url])
            return f"Opening {site.capitalize()} in Brave."
        else:
            return f"I don't know the site '{site}'. Try adding it to the list."

    return None