import json
import csv

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
        return json.load(f)

def parse_csv_log(log_file):
    with open(log_file, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def parse_txt_log(log_file):
    with open(log_file, 'r') as f:
        return f.readlines()

if __name__ == "__main__":
    sample_log_json = "../logs/sample_log1.json"
    sample_log_csv = "../logs/sample_log2.csv"
    sample_log_txt = "../logs/sample_log3.txt"

    print(parse_log_file(sample_log_json))
    print(parse_log_file(sample_log_csv))
    print(parse_log_file(sample_log_txt))
