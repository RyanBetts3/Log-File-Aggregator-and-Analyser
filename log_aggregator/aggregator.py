import os

def aggregate_logs(log_directory):
    log_files = []
    for root, dirs, files in os.walk(log_directory):
        for file in files:
            if file.endswith(('.json', '.csv', '.txt')):
                log_files.append(os.path.join(root, file))
    return log_files

if __name__ == "__main__":
    log_directory = "../logs"
    log_files = aggregate_logs(log_directory)
    for log_file in log_files:
        print(f"Found log file: {log_file}")
