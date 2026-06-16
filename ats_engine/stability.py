import time
import logging

logger = logging.getLogger(__name__)

def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.error(f"Execution failed: {e}")
        return None


def retry(func, retries=3, delay=1, *args, **kwargs):
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception:
            time.sleep(delay)

    return None