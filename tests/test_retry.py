from api.error_handling import retry_request


def test_retry():

    result = retry_request(
        lambda: 1
    )

    assert result == 1


if __name__ == "__main__":

    test_retry()

    print("All tests passed")