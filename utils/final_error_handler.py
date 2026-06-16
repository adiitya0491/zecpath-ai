"""
Day 65

Final Error Handler

Zecpath AI
"""


def safe_run(

    func,

    fallback=None

):

    try:

        return func()

    except Exception as error:

        return {

            "error": str(error),

            "fallback": fallback,

            "status": "handled"

        }


if __name__ == "__main__":

    result = safe_run(

        lambda: 10 / 0,

        "Default"

    )

    print(result)