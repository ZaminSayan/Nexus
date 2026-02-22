# backend/commands/__init__.py
from .open_command import handle_open
from .system_command import handle_time, handle_date, handle_greeting
from .utility_command import handle_calculate, handle_search, handle_joke

COMMANDS = {
    "open": handle_open,
    "time": handle_time,
    "date": handle_date,
    "greeting": handle_greeting,
    "calculate": handle_calculate,
    "search": handle_search,
    "joke": handle_joke
}