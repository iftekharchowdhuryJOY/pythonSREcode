#!/usr/bin/env python3
import argparse
import socket
import sys
import logging

def check_port(host, port, timeout=5):
    """Check if a port is open"""
    logging.debug("Creating socket...")
    try:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        logging.debug(f"Attempting connection to {host}:{port}...")
        # Try to connect
        result = sock.connect_ex((host, port))
        sock.close()
        
        return result == 0  # True if connected, False otherwise
        
    except socket.gaierror:
        # DNS resolution failed (hostname not found)
        logging.error(f"✗ Cannot resolve hostname: {host}")
        return False
    except Exception as e:
        # Any other error
        logging.error(f"✗ Error: {e}")
        return False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Check if a port is open on a host'
    )
    
    parser.add_argument('host', help='Hostname or IP address')
    parser.add_argument('--port', type=int, default=80, 
                       help='Port number (default: 80)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose (DEBUG) logging')
    
    args = parser.parse_args()
    
    # Configure logging AFTER parsing arguments
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    logging.debug("Script started")
    logging.debug(f"Arguments: host={args.host}, port={args.port}")
    logging.info(f"Checking {args.host}:{args.port}")
    
    # Check the port
    if check_port(args.host, args.port):
        logging.info(f"✓ Port {args.port} is open on {args.host}")
        logging.debug("Script completed successfully")
        sys.exit(0)  # Success
    else:
        logging.error(f"✗ Port {args.port} is closed on {args.host}")
        logging.debug("Script completed with failure")
        sys.exit(1)  # Failure

if __name__ == '__main__':
    main()