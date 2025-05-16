import json
import os

def load_event_log():
    try:
        with open("../shared_data/event_log.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def load_agents():
    try:
        with open("../shared_data/agents.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
