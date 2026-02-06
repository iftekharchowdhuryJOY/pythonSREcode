#! /usr/bin/env python3
pod_status = {
    "name": "nginx-frontend",
    "status": "running",
    "restarts": 3
}
print(pod_status["name"])

pod_status["restarts"] = 4
pod_status["node"] = "hp-elitebook"

print(pod_status)
raw_logs = ["192.168.1.10", "10.0.0.5", "192.168.1.10", "172.16.0.1", "10.0.0.5", "10.0.0.5", "192.168.1.10", "8.8.8.8"]

ip_counts = {}

for ip in raw_logs:
    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1
print(ip_counts)