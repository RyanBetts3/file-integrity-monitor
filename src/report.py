import json
import os

def generate_report(changes, output_file):
    report = {
        "summary": f"Detected {len(changes)} changes",
        "details": changes
    }
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    sample_changes = [{"path": "./monitor/test.txt", "change": "modified"}]
    output_file = "./reports/change_report.json"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    generate_report(sample_changes, output_file)
