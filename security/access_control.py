"""
Day 55
Access Control System
"""

ROLES = {
    "admin": [
        "read",
        "write",
        "delete"
    ],

    "recruiter": [
        "read",
        "write"
    ],

    "viewer": [
        "read"
    ]
}


def has_access(role, action):
    """
    Check whether a role
    can perform an action.
    """

    return action in ROLES.get(
        role,
        []
    )


if __name__ == "__main__":

    print(
        has_access(
            "admin",
            "delete"
        )
    )

    print(
        has_access(
            "viewer",
            "write"
        )
    )