import sys

# 1. Check the length FIRST to prevent a crash
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <logfile> <env>")
    sys.exit(1) # Exit because we can't continue

# 2. Now it is safe to assign variables
logfile = sys.argv[1]
env = sys.argv[2]

# 3. Success logic
print(f"Analyzing {env} logs from file: {logfile}")
# Note: Usually we sys.exit(0) for success, or just let the script finish.