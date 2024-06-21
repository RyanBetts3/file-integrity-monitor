import os
import hashlib
import json
from baseline import calculate_hash

def load_baseline():
    with open('./baseline/baseline.json', 'r') as f:
        baseline = json.load(f)
        print("Loaded baseline:", baseline)
        return baseline

def monitor_files(baseline):
    changes = []
    for file_path, metadata in baseline.items():
        if not os.path.exists(file_path):
            changes.append({"path": file_path, "change": "deleted"})
        else:
            current_hash = calculate_hash(file_path)
            if current_hash != metadata['hash']:
                changes.append({"path": file_path, "change": "modified"})
    print("Detected changes:", changes)
    return changes

if __name__ == "__main__":
    baseline = load_baseline()
    changes = monitor_files(baseline)
    for change in changes:
        print(f"File {change['path']} was {change['change']}.")
