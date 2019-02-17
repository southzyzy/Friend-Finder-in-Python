"""
Function 4:
Author: @ Tan Zhao Yea
Function 5 Ranking Metric @ Kish & Koh Jie

Using the Google Books API, the application can perform full-text searches and retrieve book information, viewability and eBook availability. You can also manage your personal bookshelves:
    -> Google Books API will return 10 search results with every requests
    -> While some books will not provide you the categories (genre) of a book, there is a need to loop through the entire request to find a genre from any book (10 books) given by the books API
    -> Looping through al the result is too inefficient, so I implement an algorithm that grab any random book with its genre, if the book doesnt contain a genre, we try again with another random integer.
    -> Limited to only 1000 request per day, to minimise the usage of API key, we will store the bookname and its genre in the file. And thus before doing the search, will first check for books without genre and then do the searching.
        Books with genre will not be parse into the API.

Together with GRequests: Asynchronous Requests, we perform Asynchronous search method to minimise the waiting time while searching for a book:
    -> The normal method to search is always one request by a request. By using grequests, we pump and search all the books in a go
    -> This helps to improve the flow of the program! Providing efficiency and reliability at the same time.

Lambda -> Use in the program mainly to filter out the response from grequests


More Info:
Google Books API: https://developers.google.com/books/
GRequests Asynchronous Requests: https://github.com/kennethreitz/grequests
Lambda: http://book.pythontips.com/en/latest/lambdas.html
"""

import os
import re
import grequests
import random
import pandas as pd


# Generate a random integer
def randomInt(num):
    return random.randint(0, num - 1)


# Class google books
class G_BOOKS():
    def __init__(self, obj, cipherText, key):
        aes = obj.AESCipher(key)  # getting the key to decrypt the api key
        self.googleapikey = aes.decrypt(key, cipherText)

    def get_book_genre(self, line):
        book_list = []  # specify the book list that will be used to store the bookname and its genre, that is the reply from the API
        urls = []  # urls list to store all the search requests

        for book_name in line:  # iterate through the booklist.txt
            if not re.findall("::.*", book_name):  # check if the book have any genre
                urls.append("https://www.googleapis.com/books/v1/volumes?q={}&key={}".format(book_name,
                                                                                             self.googleapikey))  # store all the serach url

        # Sending requests at one go.
        rs = (grequests.get(u) for u in urls)

        name = map(lambda x: re.findall('q=(.*)&', x), urls)  # store all the book name
        format_lst = [single_name for n in name for single_name in n]  # format the list to remove [] in the name list
        count = 0  # intialise a counter

        for content in grequests.map(rs):
            rjson = content.json()  # convert content object to json
            randNum = randomInt(len(rjson["items"]))  # create a random int with a given len of the book response
            book_info = rjson["items"][randNum]  # grab any random book

            # tries to get the categories of the book at most 10 times
            for i in xrange(10):
                if "categories" in book_info["volumeInfo"]:  # if genre exist in the current book, break out of the loop
                    break
                else:  # repeat the steps that create another int and then get the contents of the books
                    randNum = randomInt(len(rjson["items"]))
                    book_info = rjson["items"][randNum]

            gl = book_info["volumeInfo"]["categories"]  # finally store the gnere of the book

            # store the book and its genre in the book_list
            book_list.append({
                format_lst[count]: gl[0]
            })
            count += 1  # search the next book

        # Getting the genre out of the book and create it into the new dictionary
        # The purpose of having this is to be used in the function count_book_match where you get the genre of a book, with a given book
        book_genre_dict = {}

        for val in line:
            if not re.findall("::.*", val):
                genres_list = list(set(filter(lambda x: x is not None, map(lambda y: y.get(val),
                                                                           book_list))))  # retrieve the genre of a given book
                book_genre_dict[val] = [
                    ','.join(str(g) for g in genres_list)]  # storing the book and its dictionary seperating with a ','

        return book_genre_dict

    def writeBooks2File(self, booklist_dir, book_list):
        # store all the books in the a text file
        if not os.path.exists(booklist_dir):
            open(booklist_dir, "w").close()

        BOOKS = []  # create an empty books list
        condition = map(lambda b: b.split("|"), book_list)  # split the books with | into its individual state
        for i in condition:
            map(lambda a: BOOKS.append(a.rstrip()), i)  # append the book into BOOKS. removing white space

        BOOKS = list(set(BOOKS))  # remove duplicate books

        rf = open(booklist_dir, "r").read().splitlines()  # Returns a list of books
        af = open(booklist_dir, "a")  # Open for appending

        have_genre = []  # Create empty list to store books that alr have genre

        for book in rf:
            if re.findall("::.*", book):  # Find all books that have genre
                # Remove the genre so and add the book name that have a genre
                have_genre.append(re.sub(re.findall("::.*", book)[0], '',
                                         book).rstrip())  # add into the have_genre for books with genre

        # appending the book text file
        for val in BOOKS:
            if val not in rf and val not in have_genre:  # if the book not in file and also not have genre, insert it into the file
                af.write(val + '\n')
        af.close()

    # update the file after it find its genre
    def update_file(self, booklist_dir, old_string, new_string):
        new_string = old_string + "::" + new_string[0]
        # Safely read the input filename using 'with'
        with open(booklist_dir) as f:
            s = f.read()

        # Safely write the changed content, if found in the file
        with open(booklist_dir, 'w') as f:
            s = s.replace(old_string + "\n", new_string + "\n")  # replace the old string with the new string
            f.write(s)

    # this part count the genre that matches with student B
    def count_book_match(self, temp_list, sb_info, bk_dict):
        """ This part gets the genre that student prefers """
        sb_books = [i.strip() for i in sb_info.Books.values[0].split("|")]

        sb_genre_preferences = []  # create an empty list to store the student genre preferences
        for book in sb_books:  # loop in the books of all the books that student B read
            # get the genre of the book he/she read and append it into the sb_genre_preferences (dictionary get from get_book_genre())
            sb_genre_preferences.append(bk_dict.get(book))

        sb_genre_preferences = list(set(sb_genre_preferences))  # remove all duplicates

        # This part gets the genre that all the other data prefers
        name_books_genre = {}  # create an empty dictionary that is going to store the { name of a user : [list of genre] }
        for items in temp_list:  # loop throughout the list of all profiles
            # remove the duplicates of the list results, by passing every book the profiles read and store them inthe the name_books_genre
            name_books_genre[items["Name"]] = list(set([bk_dict.get(val.strip()) for val in items["Books"].split("|")]))

        # This part counts the score that matches their book genre
        score = {}
        count = 0

        # If the genre match, points will be added to the profile
        for key, value in name_books_genre.iteritems():
            for g in sb_genre_preferences:
                if g in value:
                    count += 1
            score[key] = count
            count = 0

        return score

    # update the score for function 4
    def matches(self, count_genre, temp_list):
        for i in temp_list:
            i["Rank"] += count_genre.get(i["Name"])

        f4_df = pd.DataFrame.from_dict(temp_list, orient='columns')

        # sort in descending order
        return f4_df.sort_values(by=["Rank"], ascending=False)
