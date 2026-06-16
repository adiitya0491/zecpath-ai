"""
Day 55
Encryption Utilities
"""

from cryptography.fernet import Fernet

# Generate key

key = Fernet.generate_key()

cipher = Fernet(key)


def encrypt_data(data):

    return cipher.encrypt(
        data.encode()
    )


def decrypt_data(token):

    return cipher.decrypt(
        token
    ).decode()


if __name__ == "__main__":

    text = "Candidate Selected"

    encrypted = encrypt_data(text)

    print(
        "Encrypted:",
        encrypted
    )

    print(
        "Decrypted:",
        decrypt_data(encrypted)
    )