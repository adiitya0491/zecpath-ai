"""
Day 57
Error Handling Utility
"""


def safe_execute(func, default=None):
    """
    Execute function safely.
    """

    try:
        return func()

    except Exception as error:

        return {
            "error": str(error),
            "fallback": default
        }


if __name__ == "__main__":

    result = safe_execute(
        lambda: 1 / 0,
        default="Operation Failed"
    )

    print(result)