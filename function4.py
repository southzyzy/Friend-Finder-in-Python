import os, sys, time
import requests
import random
from multiprocessing import Pool

import AESCipher

genreDict = {}

CURENT_DIR = os.path.dirname(__file__)  # specify current directory
API_KEY_DIR = os.path.join(CURENT_DIR, "keys/")
key_files = [file for file in os.listdir(API_KEY_DIR) if file.endswith(".bin")]  # list out the api-keys in keys folder


def randomInt(num):
    return random.randint(0, num - 1)


def search(book_name, googleapikey):
    """
    This function search the book by on its title. Returns the genre of the book
    """
    parms = {"q": book_name, 'key': googleapikey}
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

    genreDict[book_name] = gl[0]

    return genreDict


class G_BOOKS():
    def __init__(self, obj, cipherText, key):
        aes = obj.AESCipher(key)
        self.googleapikey = aes.decrypt(key, cipherText)

    def get_book_genre(self):
        book_dir = "D:/SIT/ICT-1002 Programming Fundamentals/ICT1002_Tinder/booklist.txt"
        book_file = open(book_dir, "r")
        line = book_file.read().splitlines()

        pool = Pool(processes=6)
        jobs = []
        bookLst = []

        for val in line:
            jobs.append(pool.apply_async(search, args=(val, self.googleapikey)))

        # wait for all jobs to finish
        for j in jobs:
            bookLst.append(j.get())

        pool.close()
        pool.join()

        for val in line:
            condition = filter(lambda y: y is not None, map(lambda x: x.get(val), bookLst))
            print val,
            print list(set(condition))

    def bookGenre(self, genreList, df):
        df['Books_Genre'] = ",".join(set(genreList))
        return df


if __name__ == '__main__':
    start_time = time.time()
    aes = AESCipher
    api_dir = API_KEY_DIR + key_files[0]
    api_file = open(api_dir, "r")
    enc = api_file.read()
    api_file.close()

    bk = G_BOOKS(aes, enc, sys.argv[1])
    bk.get_book_genre()

    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))
    sys.exit()
