from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64


def derive_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000,
    )

    return base64.urlsafe_b64encode(
        kdf.derive(master_password.encode())
    )


def encrypt(data: str, key: bytes) -> str:
    fernet = Fernet(key)

    return fernet.encrypt(
        data.encode()
    ).decode()


def decrypt(data: str, key: bytes) -> str:
    try:
        fernet = Fernet(key)

        return fernet.decrypt(
            data.encode()
        ).decode()

    except InvalidToken:
        raise ValueError(
            "Wrong master password or corrupted vault data."
        )