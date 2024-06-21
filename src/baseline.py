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
    baseline = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            file_metadata = {
                "path": file_path,
                "hash": file_hash,
                "size": os.path.getsize(file_path),
                "mtime": os.path.getmtime(file_path)
            }
            baseline[file_path] = file_metadata
    with open('./baseline/baseline.json', 'w') as f:
        json.dump(baseline, f, indent=4)

if __name__ == "__main__":
    create_baseline('./monitor')
