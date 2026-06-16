import datetime

def audit_log(action, user, candidate_id):

    return {
        "action": action,
        "user": user,
        "candidate_id": candidate_id,
        "timestamp": datetime.datetime.now(
            datetime.UTC
        ).isoformat()
    }

if __name__ == "__main__":

    log = audit_log(
        "decision_modified",
        "admin",
        "C101"
    )

    print(log)