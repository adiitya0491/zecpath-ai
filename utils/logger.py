from loguru import logger

# Save logs into a file inside logs folder
logger.add(
    "logs/zecpath_ai.log",
    rotation="1 MB",
    level="INFO",
    format="{time} | {level} | {message}"
)

def get_logger():
    return logger
