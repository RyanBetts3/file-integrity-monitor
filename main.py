import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from baseline import create_baseline
from monitor import load_baseline, monitor_files
from alert import send_alert
from report import generate_report

def main():
    # Create baseline if it doesn't exist
    if not os.path.exists('./baseline/baseline.json'):
        print("Creating baseline...")
        create_baseline('./monitor')
        print("Baseline created.")

    # Load baseline and monitor files
    print("Loading baseline...")
    baseline = load_baseline()
    print("Loaded baseline:", baseline)
    print("Monitoring files...")
    changes = monitor_files(baseline)

    # Alert and report changes
    if changes:
        print("Changes detected, sending alert...")
        send_alert(changes)
        print("Generating report...")
        reports_directory = "./reports"
        os.makedirs(reports_directory, exist_ok=True)
        generate_report(changes, os.path.join(reports_directory, "change_report.json"))
    else:
        print("No changes detected.")

if __name__ == "__main__":
    main()
