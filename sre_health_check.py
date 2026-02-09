def main():
        
    services = [
        {"name": "auth", "latency": 80},
        {"name": "payments", "latency": 320},
        {"name": "search", "latency": 150},
        {"name": "inventory", "latency": 400},
        {"name": "orders", "latency": 250},
    ]

    for svc in services:
        if svc["latency"] > 400:
            print(f"CRITICAL: {svc['name']} latency is HIGH ({svc['latency']}ms)")
        elif svc["latency"] >=200:
            print(f"WARNING: {svc['name']} latency is HIGH ({svc['latency']}ms)")
        else:
            print(f"OK: {svc['name']} latency normal")
if __name__ == "__main__":
    main()