from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import b64encode, b64decode
from os import urandom
from cryptography.fernet import Fernet

BS = 16
def pad(s): return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
def unpad(s): return s[0:-ord(s[-1])]


def generateKey():
    random_b = urandom(32)
    return b64encode(random_b)


def generateIV():
    return urandom(16)


def encrypt(key, message):
    iv = generateIV()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(message + encryptor.finalize()

    print(f'Message encrypted: {encrypted}')
    print(f'Key: {key}')
    return encrypted
