raw_logs = ["192.168.1.10", "10.0.0.5", "192.168.1.10", "172.16.0.1", "10.0.0.5", "10.0.0.5", "192.168.1.10", "8.8.8.8"]

total_count = len(raw_logs)
unique_ips = set(raw_logs)
unique_count = len(unique_ips)

# Using unique_count for a cleaner sentence
print(f"Detected {unique_count} unique IPs out of {total_count} total requests.")

# Check if unique IPs are less than 50% of total traffic
if unique_count < (total_count / 2):
    print("ALERT: High duplicate traffic detected!")
else:
    print("Traffic levels look normal.")