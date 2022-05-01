"""
Decorator with runtime logging
"""
import logging
import time
from functools import wraps
# Import module logging, time and from functools packages wraps.

logger = logging.getLogger(__name__)

# Set the settings for the logger to output the report to the terminal.
logger.setLevel("DEBUG")
handler = logging.StreamHandler()
LOG_FORMAT = "%(asctime)s %(levelname)s -- %(message)s"
formatter = logging.Formatter(LOG_FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)


def timed(func):
    """This decorator prints the execution time for the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.debug(f"{func.__name__} ran in {round(end_time - start_time, 2)} s")
        return result

    return wrapper


@timed
def slow_function():
    """This is a slow-running function used as an example."""
    print("Running a slow function...")
    time.sleep(1.5)
    print("Done!")


if __name__ == "__main__":
    slow_function()
