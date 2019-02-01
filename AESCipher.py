import base64
import hashlib
import sys
from Crypto import Random
from Crypto.Cipher import AES
from passlib.hash import sha256_crypt


class AESCipher(object):

    def __init__(self, key):
        self.bs = 32
        self.hash_key = sha256_crypt.encrypt(key)
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        cipherText = iv + cipher.encrypt(raw)
        b64_cipherText = base64.b64encode(cipherText)
        return self.hash_key + "::" + b64_cipherText

    def decrypt(self, pass_phrase, enc):
        hash_key = enc.split("::")[0]
        b64_cipherText = enc.split("::")[1]

        if sha256_crypt.verify(pass_phrase, hash_key):
            enc = base64.b64decode(b64_cipherText)
            iv = enc[:AES.block_size]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

        else:
            print "Incorrect passphrase entered."
            sys.exit(0)

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]
