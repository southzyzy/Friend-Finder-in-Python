import os
import requests
import random

# The path where the dating profiles are stored
CURENT_DIR = os.path.dirname(__file__)  # specify current directory
PROFILES = os.path.join(CURENT_DIR, "profile/")  # locate the data profile
API_KEY = os.path.join(CURENT_DIR, "keys/")
pro_files = [file for file in os.listdir(PROFILES) if file.endswith(".txt")]
genreList = []


def randomInt(num):
    return random.randint(0, num - 1)


class G_BOOKS():
    def __init__(self, obj, cipherText, key):
        aes = obj.AESCipher(key)
        self.googleapikey = aes.decrypt(key, cipherText)

    def search(self, book_name):
        """
        This function search the book by on its title. Functions of this function:
        1.


        :param book_name:
        :return:
        """
        parms = {"q": book_name, 'key': self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        rjson = r.json()

        randNum = randomInt(len(rjson["items"]))
        book_info = rjson["items"][randNum]

        # Try and search for the categories for 10 times
        for i in xrange(10):
            if "categories" in book_info["volumeInfo"]:
                break
            else:
                randNum = randomInt(len(rjson["items"]))
                book_info = rjson["items"][randNum]

        gl = book_info["volumeInfo"]["categories"]

        genreList.append(book_name + "-" + gl[0])

        return genreList

    def compareBooks(self):
        print "HelloWorld"
