import re
import requests
import random
from multiprocessing import Pool
import pandas as pd


def randomInt(num):
    return random.randint(0, num - 1)


def search(book_name, googleapikey):
    """
    This function search the book by on its title. Returns the genre of the book
    """
    genreDict = {}

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

    def get_book_genre(self, line):
        pool = Pool(processes=6)
        jobs = []
        book_list = []

        for val in line:
            if not re.findall("::.*", val):
                jobs.append(pool.apply_async(search, args=(val, self.googleapikey)))

        # wait for all jobs to finish
        for j in jobs:
            book_list.append(j.get())

        pool.close()
        pool.join()

        # Getting the genre out of the book and create it into the new dictionary
        book_genre_dict = {}

        for val in line:
            if not re.findall("::.*", val):
                genres_list = list(set(filter(lambda x: x is not None, map(lambda y: y.get(val), book_list))))
                book_genre_dict[val] = [','.join(str(g) for g in genres_list)]

        return book_genre_dict

    def update_file(self, booklist_dir, old_string, new_string):
        new_string = old_string + "::" + new_string[0]
        # Safely read the input filename using 'with'
        with open(booklist_dir) as f:
            s = f.read()

        # Safely write the changed content, if found in the file
        with open(booklist_dir, 'w') as f:
            s = s.replace(old_string + "\n", new_string + "\n")
            f.write(s)

    def count_book_match(self, temp_list, sb_info, bk_dict):
        """ This part gets the genre that student prefers """
        sb_books = [i.strip() for i in sb_info.Books.values[0].split("|")]

        sb_genre_preferences = []
        for book in sb_books:
            sb_genre_preferences.append(bk_dict.get(book))

        sb_genre_preferences = list(set(sb_genre_preferences))

        """ This part gets the genre that all the other data prefers """
        name_books_genre = {}
        for items in temp_list:
            name_books_genre[items["Name"]] = list(set([bk_dict.get(val.strip()) for val in items["Books"].split("|")]))

        """ This part counts the score that matches their book genre """
        score = {}
        count = 0
        for key, value in name_books_genre.iteritems():
            # print key,
            # print value
            for g in sb_genre_preferences:
                if g in value:
                    # print g
                    count += 1
            # print count
            score[key] = count
            count = 0

        print score
        return score

    def matches(self, count_genre, temp_list):
        for i in temp_list:
            i["Rank"] += count_genre.get(i["Name"])

        f4_df = pd.DataFrame.from_dict(temp_list, orient='columns')
        return f4_df.sort_values(by=["Rank"], ascending=False)
