#Example: Managing multiple servers
infrastructure = {
    "web_server": {
        "os": "Ubuntu 22.04",
        "ip": "192.168.1.10",
        "status": "active"
    },
    "db_server": {
        "os": "Debian",
        "ip": "192.168.1.20",
        "status": "maintenance"
    }
}

# Accessing a nested value


for k, v in infrastructure.items():
    print(f"{k}: {v}")
