from ai_core.release_ready_system import (

    release_pipeline

)


def test_release():

    result = release_pipeline(

        "C1",

        {

            "ats": 120,

            "hr": -10

        }

    )

    assert result["final_score"] >= 0


if __name__ == "__main__":

    test_release()

    print(

        "All tests passed"

    )