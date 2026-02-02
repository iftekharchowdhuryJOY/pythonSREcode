import socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.setdefaulttimeout(5)

host = "google.com"
port = 80

result = sock.connect_ex((host, port))

if result == 0:
    print(f"port connected to {host} on port {port}")
else:
    print(f"port {port} is not connected to {host}")

sock.close()