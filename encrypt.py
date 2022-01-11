from cryptography.fernet import Fernet
import base64


def encrypt(key, message):
    fern = Fernet(key)
    return fern.encrypt(message.encode())


def decrypt(key, message):
    fern = Fernet(key)
    return fern.decrypt(message.encode())


def generateKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def loadKey():
    key = open("key.key", "rb").read()
    return key
