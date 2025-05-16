import json
import random
import time
from datetime import datetime

# Read JSON file
def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Simulate random status updates
def simulate_updates(data, key, choices):
    for entry in data:
        if random.random() < 0.3:  # 30% chance to update
            entry[key] = random.choice(choices)
            if 'timestamp' in entry:
                entry['timestamp'] = datetime.utcnow().isoformat() + "Z"
    return data
