import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from screening_ai.report_generator import generate_screening_report


def test_system():

    report = generate_screening_report(
        candidate_id="C1",
        job_id="J1",
        answers=[],
        scores=[],
        behavior_reports=[]
    )

    assert "candidate_id" in report