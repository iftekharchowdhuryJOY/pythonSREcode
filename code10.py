import sys
import json 

if len(sys.argv) != 2:
    print("Usage: python code10.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
counts = {}

try:
    with open(filename, 'r') as file:
        for line in file:
            service = line.strip()
            if not service:
                continue
            
            if service in counts:
                counts[service] +=1
            else:
                counts[service] = 1
    json_report = json.dumps(counts, indent=4)
    print(json_report)
   
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  
