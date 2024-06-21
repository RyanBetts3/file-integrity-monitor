def send_alert(changes):
    for change in changes:
        print(f"ALERT: File {change['path']} was {change['change']}.")

if __name__ == "__main__":
    sample_changes = [{"path": "./monitor/test.txt", "change": "modified"}]
    send_alert(sample_changes)
