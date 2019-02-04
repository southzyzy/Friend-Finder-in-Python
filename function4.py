import requests
import AESCipher
import os, sys, time
import pandas as pd
import random
import student_B as sb
import function1 as f1
import numpy as np

# The path where the dating profiles are stored
CURENT_DIR = os.path.dirname(__file__)  # specify current directory
PROFILES = os.path.join(CURENT_DIR, "profile/")  # locate the data profile
API_KEY = os.path.join(CURENT_DIR, "keys/")
pro_files = [file for file in os.listdir(PROFILES) if file.endswith(".txt")]


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
        rj = r.json()

        randNum = randomInt(len(rj["items"]))

        book_info = rj["items"][randNum]
        # book_url = "https://www.googleapis.com/books/v1/volumes/" + book_id + "?key=" + self.googleapikey + "&fields=volumeInfo/categories"
        print book_name
        print r.url

        # req = requests.get(book_url)
        # book_info = req.json()

        genreList = [book_name]
        gl = book_info["volumeInfo"]["categories"]

        # select a random index and choose the category
        ranIndex = randomInt(len(gl))
        gl = gl[ranIndex]
        genreList.append(gl)

        # genre_df = pd.DataFrame([genreList], columns=["Book", "Genre"])
        # genre_df["Genre"] = genre_df.Genre.str.replace(" / ", ",")
        print genreList


if __name__ == "__main__":
    start_time = time.time()
    aes = AESCipher

    filename = "D:/SIT/ICT-1002 Programming Fundamentals/ICT1002_Tinder\keys/api-key.txt.bin"
    input_file = open(filename, "r")
    enc = input_file.read()
    input_file.close()

    profiles_list = f1.FUNCTION_1(profiles=PROFILES, files=pro_files)
    profiles_df = profiles_list.profilesDF(profiles_list.HEADERS, profiles_list.DATA)

    # student_B_name = "Yulanda Martinez"
    # student_B_info = sb.STUDENT_B(profiles_df)
    # student_B_info = student_B_info.check_name(student_B_name)
    # print student_B_info["Books"].values


    bk = G_BOOKS(aes, enc, sys.argv[1])
    for i in profiles_df.Books.values:
        for a in  i.split(","):
            bk.search(a)
    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))
