import datetime

def log_event(service, event_type, data):

    return {
        "service": service,
        "event_type": event_type,
        "data": data,
        "timestamp": datetime.datetime.now(
            datetime.UTC
        ).isoformat()
    }

if __name__ == "__main__":

    log = log_event(
        "ATS",
        "score_generated",
        {
            "candidate_id": "C101",
            "score": 78
        }
    )

    print(log)