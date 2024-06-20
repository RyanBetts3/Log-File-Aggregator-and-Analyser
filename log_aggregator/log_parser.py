import json
import csv
import pandas as pd

def parse_log_file(log_file):
    if log_file.endswith('.json'):
        return parse_json_log(log_file)
    elif log_file.endswith('.csv'):
        return parse_csv_log(log_file)
    elif log_file.endswith('.txt'):
        return parse_txt_log(log_file)
    else:
        raise ValueError(f"Unsupported log format: {log_file}")

def parse_json_log(log_file):
    with open(log_file, 'r') as f:
        data = json.load(f)
        for entry in data:
            entry['timestamp'] = pd.to_datetime(entry['timestamp'])
        return data

def parse_csv_log(log_file):
    df = pd.read_csv(log_file, parse_dates=['timestamp'])
    return df.to_dict('records')

def parse_txt_log(log_file):
    log_data = []
    with open(log_file, 'r') as f:
        for line in f:
            timestamp, message = line.split(' ', 1)
            log_data.append({"timestamp": pd.to_datetime(timestamp), "message": message.strip()})
    return log_data

if __name__ == "__main__":
    sample_log_json = "../logs/sample_log1.json"
    sample_log_csv = "../logs/sample_log2.csv"
    sample_log_txt = "../logs/sample_log3.txt"

    print(parse_log_file(sample_log_json))
    print(parse_log_file(sample_log_csv))
    print(parse_log_file(sample_log_txt))
