import os
import hashlib
import json

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def create_baseline(directory):
    print(f"Creating baseline for directory: {directory}")
    baseline = {}
    for root, dirs, files in os.walk(directory):
        print(f"Scanning directory: {root}")
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Processing file: {file_path}")
            file_hash = calculate_hash(file_path)
            file_metadata = {
                "path": file_path,
                "hash": file_hash,
                "size": os.path.getsize(file_path),
                "mtime": os.path.getmtime(file_path)
            }
            baseline[file_path] = file_metadata
            print(f"Added file to baseline: {file_path}")
    with open('./baseline/baseline.json', 'w') as f:
        json.dump(baseline, f, indent=4)
    print("Baseline created:", baseline)

if __name__ == "__main__":
    create_baseline('./monitor')
