"""
Day 57
Stable API Response Layer
"""


def api_response(
    success=True,
    data=None,
    error=None
):
    """
    Standard API format.
    """

    return {
        "success": success,
        "data": data if success else None,
        "error": error if not success else None
    }


if __name__ == "__main__":

    success_response = api_response(
        success=True,
        data={
            "score": 85
        }
    )

    error_response = api_response(
        success=False,
        error="Invalid Input"
    )

    print(success_response)
    print(error_response)