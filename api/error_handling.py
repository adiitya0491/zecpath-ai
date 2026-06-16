import time


def retry_request(func, retries=3, delay=1):
    """
    Retry failed API requests.
    """

    for attempt in range(retries):

        try:
            return func()

        except Exception:

            if attempt < retries - 1:
                time.sleep(delay)

    return {
        "error_code": "PROCESSING_FAILED",
        "message": "Unable to process request",
        "retry": False
    }


if __name__ == "__main__":

    result = retry_request(lambda: 1)

    print(result)