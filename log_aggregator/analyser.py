def detect_anomalies(log_data):
    anomalies = []
    # Example heuristic: count the number of entries per second
    entry_count = {}
    for entry in log_data:
        timestamp = entry.get('timestamp') or entry.get('time') or entry.get('date')
        if timestamp:
            entry_count[timestamp] = entry_count.get(timestamp, 0) + 1

    # Identify spikes in log entries
    for timestamp, count in entry_count.items():
        if count > threshold:
            anomalies.append((timestamp, count))
    
    return anomalies

if __name__ == "__main__":
    sample_log_data = [
        {"timestamp": "2024-06-20T12:00:00Z", "message": "Login attempt"},
        {"timestamp": "2024-06-20T12:00:00Z", "message": "Login attempt"},
        {"timestamp": "2024-06-20T12:00:01Z", "message": "Login attempt"},
        {"timestamp": "2024-06-20T12:00:02Z", "message": "Login attempt"},
    ]
    threshold = 2
    anomalies = detect_anomalies(sample_log_data)
    for anomaly in anomalies:
        print(f"Anomaly detected: {anomaly}")
