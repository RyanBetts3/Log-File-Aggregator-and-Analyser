import json

def generate_report(anomalies, output_file):
    report = {
        "summary": f"Detected {len(anomalies)} anomalies",
        "details": anomalies
    }

    with open(output_file, 'w') as f:
        json.dump(report, f, indent=4)

    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    sample_anomalies = [
        ("2024-06-20T12:00:00Z", 3),
        ("2024-06-20T12:00:02Z", 4),
    ]
    output_file = "../reports/anomaly_report.json"
    generate_report(sample_anomalies, output_file)
