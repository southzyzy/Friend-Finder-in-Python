import os
import re
import grequests
import random
from multiprocessing import Pool
import pandas as pd


def randomInt(num):
    return random.randint(0, num - 1)


class G_BOOKS():
    def __init__(self, obj, cipherText, key):
        aes = obj.AESCipher(key)
        self.googleapikey = aes.decrypt(key, cipherText)

    def get_book_genre(self, line):
        book_list = []
        urls = []

        for book_name in line:
            if not re.findall("::.*", book_name):
                urls.append("https://www.googleapis.com/books/v1/volumes?q={}&key={}".format(book_name, self.googleapikey))

        # Sending requests at one go.
        rs = (grequests.get(u) for u in urls)

        name = map(lambda x: re.findall('q=(.*)&', x), urls)
        format_lst = [single_name for n in name for single_name in n]
        count = 0

        for content in grequests.map(rs):
            rjson = content.json()
            randNum = randomInt(len(rjson["items"]))
            book_info = rjson["items"][randNum]

            for i in xrange(10):
                if "categories" in book_info["volumeInfo"]:
                    break
                else:
                    randNum = randomInt(len(rjson["items"]))
                    book_info = rjson["items"][randNum]

            gl = book_info["volumeInfo"]["categories"]

            book_list.append({
                format_lst[count]: gl[0]
            })
            count += 1

        # Getting the genre out of the book and create it into the new dictionary
        book_genre_dict = {}

        for val in line:
            if not re.findall("::.*", val):
                genres_list = list(set(filter(lambda x: x is not None, map(lambda y: y.get(val), book_list))))
                book_genre_dict[val] = [','.join(str(g) for g in genres_list)]

        return book_genre_dict

    def writeBooks2File(self, booklist_dir, book_list):
        # store all the books in the a text file
        if not os.path.exists(booklist_dir):
            open(booklist_dir, "w").close()

        BOOKS = []
        condition = map(lambda b: b.split("|"), book_list)
        for i in condition:
            map(lambda a: BOOKS.append(a.rstrip()), i)

        BOOKS = list(set(BOOKS))

        rf = open(booklist_dir, "r").read().splitlines()  # Returns a list
        af = open(booklist_dir, "a")

        have_genre = []  # Create empty list to store books that alr have genre

        for book in rf:
            if re.findall("::.*", book):  # Find all books that have genre
                # Remove the genre so and add the book name that have a genre
                have_genre.append(re.sub(re.findall("::.*", book)[0], '', book).rstrip())

        for val in BOOKS:
            if val not in rf and val not in have_genre:
                af.write(val + '\n')
        af.close()

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

        return score

    def matches(self, count_genre, temp_list):
        for i in temp_list:
            i["Rank"] += count_genre.get(i["Name"])

        f4_df = pd.DataFrame.from_dict(temp_list, orient='columns')
        return f4_df.sort_values(by=["Rank"], ascending=False)
