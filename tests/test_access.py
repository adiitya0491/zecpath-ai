"""
Day 55
Security Tests
"""

from security.access_control import (
    has_access
)

from security.audit_log import (
    log_event
)

from security.encryption import (
    encrypt_data,
    decrypt_data
)


def test_admin_access():

    assert has_access(
        "admin",
        "delete"
    ) is True


def test_viewer_access():

    assert has_access(
        "viewer",
        "write"
    ) is False


def test_audit_log():

    result = log_event(
        "test",
        "C1",
        {}
    )

    assert "timestamp" in result


def test_encryption():

    text = "Hello"

    encrypted = encrypt_data(text)

    decrypted = decrypt_data(
        encrypted
    )

    assert decrypted == text


if __name__ == "__main__":

    test_admin_access()

    test_viewer_access()

    test_audit_log()

    test_encryption()

    print(
        "All tests passed"
    )