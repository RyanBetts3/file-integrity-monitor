# File Integrity Monitoring Tool

## Overview
The File Integrity Monitoring Tool detects unauthorised changes to critical files by creating a baseline of file states and monitoring for any deviations. This helps in identifying potential security breaches or unauthorised activities.

## Features
- **Baseline Creation**: Generate a baseline of the current state of critical files.
- **Monitoring**: Continuously monitor files for changes.
- **Alerting**: Alert the user when unauthorised changes are detected.
- **Reporting**: Generate detailed reports of detected changes.

## Usage
1. **Prepare Files**: Place the files to be monitored in the `monitor` directory.
2. **Run the Tool**: Execute the `main.py` script to create a baseline and start monitoring.
3. **View Outputs**: Check the console for alerts and the `reports` directory for detailed reports.

## Getting Started
1. Clone the repository:
    ```sh
    git clone https://github.com/RyanBetts3/file-integrity-monitor.git
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the main script:
    ```sh
    python main.py
    ```


