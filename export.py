# export.py

import json
from datetime import datetime
import os

def export_to_json(data, username):
    folder = "output"
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = f"{folder}/{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✅ Data exported to {filename}")
