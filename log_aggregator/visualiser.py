import matplotlib.pyplot as plt

def visualise_log_data(log_data):
    timestamps = [entry['timestamp'] for entry in log_data]
    messages = [entry['message'] for entry in log_data]

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, messages, marker='o')
    plt.xlabel('Timestamp')
    plt.ylabel('Log Messages')
    plt.title('Log Data Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    sample_log_data = [
        {"timestamp": "2024-06-20T12:00:00Z", "message": 1},
        {"timestamp": "2024-06-20T12:00:01Z", "message": 2},
        {"timestamp": "2024-06-20T12:00:02Z", "message": 1},
        {"timestamp": "2024-06-20T12:00:03Z", "message": 3},
    ]
    visualise_log_data(sample_log_data)
