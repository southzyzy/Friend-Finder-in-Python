import requests
import AESCipher
import os, sys

# The path where the dating profiles are stored
CURENT_DIR = os.path.dirname(__file__)  # specify current directory
profile_directory = os.path.join(CURENT_DIR, "keys/")


class G_BOOKS():
    def __init__(self, obj, cipherText, key):
        aes = obj.AESCipher(key)
        self.googleapikey = aes.decrypt(key, cipherText)

    def search(self, value):
        parms = {"q": value, 'key': self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        print r.url
        rj = r.json()
        print rj["totalItems"]
        for i in rj["items"]:
            try:
                print repr(i["volumeInfo"]["description"])
            except:
                pass
            try:
                print repr(i["volumeInfo"]["imageLinks"]["thumbnail"])
            except:
                pass


if __name__ == "__main__":
    aes = AESCipher
    files = [file for file in os.listdir(profile_directory) if file.endswith(".bin")]
    for file in files:
        filename = profile_directory + file

        input_file = open(filename, "rb")
        enc = input_file.read()
        input_file.close()

        bk = G_BOOKS(aes, enc, sys.argv[1])
        bk.search("Bared to You")
