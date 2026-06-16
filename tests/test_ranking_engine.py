import os
import json
from ranking.ranking_engine import rank_candidates


INPUT_FOLDER = "outputs/ats_scores/Cloud Infrastruture Engineer resumes"
OUTPUT_FILE = "outputs/candidate_ranking/cloud_Infrastructure_engineer_ranking.json"


def run():

    print("\n=== CANDIDATE RANKING ENGINE ===\n")

    ranked = rank_candidates(INPUT_FOLDER)

    os.makedirs("outputs/candidate_ranking", exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(ranked, f, indent=4)

    print("Ranking saved →", OUTPUT_FILE)


if __name__ == "__main__":
    run()