import os
from baseline import create_baseline
from monitor import load_baseline, monitor_files
from alert import send_alert
from report import generate_report

def main():
    # Create baseline if it doesn't exist
    if not os.path.exists('./baseline/baseline.json'):
        create_baseline('./monitor')

    # Load baseline and monitor files
    baseline = load_baseline()
    changes = monitor_files(baseline)

    # Alert and report changes
    if changes:
        send_alert(changes)
        reports_directory = "./reports"
        os.makedirs(reports_directory, exist_ok=True)
        generate_report(changes, os.path.join(reports_directory, "change_report.json"))

if __name__ == "__main__":
    main()
