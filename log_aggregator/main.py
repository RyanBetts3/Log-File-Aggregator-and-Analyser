import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from aggregator import aggregate_logs
from log_aggregator.log_parser import parse_log_file
from analyser import detect_anomalies
from visualiser import visualize_log_data
from reporter import generate_report

def main():
    log_directory = "./logs"
    log_files = aggregate_logs(log_directory)
    
    all_log_data = []
    for log_file in log_files:
        log_data = parse_log_file(log_file)
        all_log_data.extend(log_data)
    
    anomalies = detect_anomalies(all_log_data)
    visualize_log_data(all_log_data)
    generate_report(anomalies, "./reports/anomaly_report.json")

if __name__ == "__main__":
    main()
