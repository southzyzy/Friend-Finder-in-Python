import requests
import random

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

        genreList.append(gl[0])
        print list(set(genreList))

    def sbBookGenre(self, genreList, df):
        df['Books_Genre'] = ",".join(set(genreList))
        return df
