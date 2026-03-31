import os
import json


def rank_candidates(input_folder):

    candidates = []

    files = [f for f in os.listdir(input_folder) if f.endswith(".json")]

    for file in files:

        path = os.path.join(input_folder, file)

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        score = data.get("ats_score", 0)

        candidates.append({
            "resume": file,
            "ats_score": score
        })

    # -------------------------
    # SORT BY ATS SCORE
    # -------------------------
    candidates.sort(key=lambda x: x["ats_score"], reverse=True)

    for i, candidate in enumerate(candidates):

        rank = i + 1
        score = candidate["ats_score"]

        if score >= 0.75:
            zone = "SHORTLIST"
        elif score >= 0.60:
            zone = "REVIEW"
        else:
            zone = "REJECT"

        candidate["rank"] = rank
        candidate["zone"] = zone

    return candidates