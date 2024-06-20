import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'log_aggregator')))

from aggregator import aggregate_logs
from log_parser import parse_log_file
from analyser import detect_anomalies
from visualiser import visualise_log_data
from reporter import generate_report

def main():
    log_directory = "./logs"
    log_files = aggregate_logs(log_directory)
    
    all_log_data = []
    for log_file in log_files:
        log_data = parse_log_file(log_file)
        print(f"Parsed data from {log_file}: {log_data}")
        all_log_data.extend(log_data)
    
    anomalies = detect_anomalies(all_log_data)
    print(f"Detected anomalies: {anomalies}")
    visualise_log_data(all_log_data)
    generate_report(anomalies, "./reports")

if __name__ == "__main__":
    main()
