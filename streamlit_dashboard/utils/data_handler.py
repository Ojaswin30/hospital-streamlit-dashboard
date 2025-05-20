import json
import random
import time
from datetime import datetime

# Read JSON file
def load_json(file_path):
    """
    Load and parse JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: Parsed JSON data as a list of dictionaries.
    """
    with open(file_path, "r") as f:
        return json.load(f)


# Simulate random status updates
def simulate_updates(data, key, choices):
    """
    Randomly updates a specified key in each dictionary entry of the data with a value chosen from given options.
    Has a 30% chance to update each entry.

    If the entry contains a 'timestamp' key, update it to the current UTC time in ISO format.

    Args:
        data (list): List of dictionaries representing JSON data.
        key (str): The dictionary key to update.
        choices (list): List of possible values to assign to the key.

    Returns:
        list: The updated data list.
    """
    for entry in data:
        if random.random() < 0.3:  # 30% chance to update
            entry[key] = random.choice(choices)
            if 'timestamp' in entry:
                entry['timestamp'] = datetime.utcnow().isoformat() + "Z"
    return data
