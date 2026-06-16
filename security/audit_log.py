from datetime import datetime, UTC

def log_event(
    event_type,
    candidate_id,
    data
):
    return {
        "event_type": event_type,
        "candidate_id": candidate_id,
        "data": data,
        "timestamp": datetime.now(UTC).isoformat()
    }

if __name__ == "__main__":

    log = log_event(
        "decision_generated",
        "C15001",
        {
            "decision":
                "Selected",

            "score":
                82
        }
    )

    print(log)