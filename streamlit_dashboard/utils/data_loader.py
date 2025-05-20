import json
import os

def load_event_log():
    """
    Load event log data from a JSON file.

    Tries to read the JSON file located at '../shared_data/event_log.json'.
    If the file is not found, returns an empty list.

    Returns:
        list: Parsed event log data or an empty list if file is missing.
    """
    try:
        with open("../shared_data/event_log.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def load_agents():
    """
    Load agent data from a JSON file.

    Tries to read the JSON file located at '../shared_data/agents.json'.
    If the file is not found, returns an empty list.

    Returns:
        list: Parsed agent data or an empty list if file is missing.
    """
    try:
        with open("../shared_data/agents.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
