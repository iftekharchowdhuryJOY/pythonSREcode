#!/usr/bin/env python3
import argparse
import socket
import sys

def check_port(host, port, timeout=5):
    """Check if a port is open"""
    try:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # Try to connect
        result = sock.connect_ex((host, port))
        sock.close()
        
        return result == 0  # True if connected, False otherwise
        
    except socket.gaierror:
        # DNS resolution failed (hostname not found)
        print(f"✗ Cannot resolve hostname: {host}")
        return False
    except Exception as e:
        # Any other error
        print(f"✗ Error: {e}")
        return False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Check if a port is open on a host'
    )
    
    parser.add_argument('host', help='Hostname or IP address')
    parser.add_argument('--port', type=int, default=80, 
                       help='Port number (default: 80)')
    
    args = parser.parse_args()
    
    # Check the port
    if check_port(args.host, args.port):
        print(f"✓ Port {args.port} is open on {args.host}")
        sys.exit(0)  # Success
    else:
        print(f"✗ Port {args.port} is closed on {args.host}")
        sys.exit(1)  # Failure

if __name__ == '__main__':
    main()