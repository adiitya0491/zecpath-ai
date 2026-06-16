from ai_core.final_production_system import (

    production_pipeline

)


def test_production():

    result = production_pipeline(

        "C1",

        {

            "ats": 90,

            "hr": 80

        }

    )

    assert result["decision"] in [

        "Selected",

        "Hold / Review",

        "Rejected"

    ]


if __name__ == "__main__":

    test_production()

    print(

        "All tests passed"

    )