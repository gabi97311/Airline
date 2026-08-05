import hashlib
import os

class Hash:
    @staticmethod
    def getHash(user_password: str):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', user_password.encode('utf-8'), salt, 100000)
        return salt, key

    @staticmethod
    def get_hash_to_auth(salt, user_password: str):
        key = hashlib.pbkdf2_hmac('sha256', user_password.encode('utf-8'), salt, 100000)
        return key