import logging

logger = logging.getLogger("sre_tool")
logger.setLevel(logging.DEBUG)


# Console handler

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# File handler
file_handler = logging.FileHandler("sre_tool.log")
file_handler.setLevel(logging.DEBUG)


file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.debug("checking service auth")
services = [
    {"name": "auth", "latency": 80},
    {"name": "payments", "latency": 320},
]
for svc in services:
    logger.debug("checking service %s", svc["name"])
    if svc["latency"] > 100:
        logger.error("service %s is slow", svc["name"])
    else:
        logger.info("service %s is fast", svc["name"])

logger.info("Info message")
logger.error("Error message")

def main():
    if __name__ == "__main__":
        main()