def main():
    print(" SRE tool starting ..")
    print("system is reachable")
    service_name = "api-service"
    status = "healthy"
    latency_ms = 120
    
    print(f"service: {service_name}")
    print(f"Status: {status}")
    print(f"Latency: {latency_ms}ms")
    
    services = [
        {"name": "auth", "latency": 80, "status": "healthy"},
        {"name": "payments", "latency": 320, "status": "degraded"},
        {"name": "search", "latency": 150, "status": "healthy"},
    ]
    
    for svc in services:
        print(f"{svc['name']} | {svc['status']} | {svc['latency']}ms")
        
    services = [
        {"name": "auth", "latency": 80},
        {"name": "payments", "latency": 320},
        {"name": "search", "latency": 150},
    ]

    for svc in services:
        if svc["latency"] > 300:
            print(f"ALERT: {svc['name']} latency is HIGH ({svc['latency']}ms)")
        else:
            print(f"OK: {svc['name']} latency normal")
if __name__ == "__main__":
    main()