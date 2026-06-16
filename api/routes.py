from flask import Flask, request, jsonify
from screening_ai.report_generator import generate_screening_report

app = Flask(__name__)

@app.route("/screening/start", methods=["POST"])
def start_screening():
    data = request.json

    candidate_id = data.get("candidate_id")
    job_id = data.get("job_id")
    answers = data.get("answers", [])
    scores = data.get("scores", [])
    behavior_reports = data.get("behavior", [])

    report = generate_screening_report(
        candidate_id=candidate_id,
        job_id=job_id,
        answers=answers,
        scores=scores,
        behavior_reports=behavior_reports
    )

    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=True)