from demo.full_pipeline_simulation import (

    run_demo_pipeline

)


def test_demo():

    result = run_demo_pipeline(

        "C001"

    )

    assert (

        result["result"]["decision"]

        ==

        "Selected"

    )


if __name__ == "__main__":

    test_demo()

    print(

        "All tests passed"

    )