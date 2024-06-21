# File Integrity Monitoring Tool

## Overview
The File Integrity Monitoring Tool is designed to detect unauthorised changes to critical files on a system. It helps in identifying potential security breaches or unauthorised activities by monitoring and reporting any modifications to critical files. This tool is useful for system administrators and security professionals to maintain the integrity of critical files and quickly respond to potential incidents.

## Features
- **Baseline Creation**: Generate a baseline of the current state of critical files, including their hashes and metadata.
- **Monitoring**: Continuously monitor files for any changes compared to the baseline.
- **Alerting**: Alert the user when unauthorised changes are detected.
- **Reporting**: Generate detailed reports of detected changes.

## Usage

### Prerequisites
- Python 3.x
- Any required Python packages will be listed in `requirements.txt`

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/RyanBetts3/file-integrity-monitor.git
    cd file-integrity-monitor
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Preparing Files
1. Create a directory named `monitor` in the root of the project if it does not exist:
    ```sh
    mkdir monitor
    ```

2. Add the files you want to monitor into the `monitor` directory.

### Running the Tool
1. **Create Baseline**: If running for the first time or when files are added/removed, create a baseline:
    ```sh
    python src/baseline.py
    ```

2. **Monitor Files**: Run the main script to monitor files and detect changes:
    ```sh
    python main.py
    ```

### Viewing Reports
1. If changes are detected, a report will be generated in the `reports` directory. Open the generated `change_report.json` file to view details of the changes:
    ```sh
    cat ./reports/change_report.json
    ```

## Example Workflow
1. **Setup and Installation**:
    ```sh
    git clone https://github.com/RyanBetts3/file-integrity-monitor.git
    cd file-integrity-monitor
    pip install -r requirements.txt
    mkdir monitor
    echo "Initial content" > monitor/test1.txt
    echo "Initial content" > monitor/test2.txt
    ```

2. **Create Baseline**:
    ```sh
    python src/baseline.py
    ```

3. **Modify a File**:
    ```sh
    echo "This is a test modification." > monitor/test1.txt
    ```

4. **Monitor Files and Generate Report**:
    ```sh
    python main.py
    ```

5. **View Report**:
    ```sh
    cat ./reports/change_report.json
    ```

