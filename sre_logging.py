'''
Python’s logging module is a structured event reporting system.
It is a tool for developers to debug and monitor the code.
basicConfig() is a quick setup function. It configures the root logger with default behavior.
| Token           | Meaning      |
| --------------- | ------------ |
| `%(asctime)s`   | Timestamp    |
| `%(levelname)s` | Log severity |
| `%(message)s`   | Your message |
| `%(name)s`      | Logger name  |
| `%(filename)s`  | File name    |
| `%(lineno)d`    | Line number  |

'''
import logging
# Any logs that don’t have custom config — behave like this.

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
'''
If level = INFO:

DEBUG → hidden

INFO → shown

WARNING → shown

ERROR → shown

CRITICAL → shown

If level = DEBUG:

Everything shows.
'''
logger = logging.getLogger(__name__)

print(logger.name)
print(logger.level)
