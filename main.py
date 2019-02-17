"""
MAIN Method:
Author: Tan Zhao Yea

This part holds all the codes to make the Friend Finder app workable. It hold many functions in a class, namely:
    1. getAPIKey() -> retrieve the API KEY
    2. MAIN class method for the ui.py to call and use the functions written in it
    3. updateBookGenre(password) -> takes in the password of the encrypted API key file and run the necessary function to acheieve function 4
    4. student_B -> returns the information of a selected student B
    5. function2() -> return the matches of acceptable country for a selected student B
    6. function3() -> takes in the result from function2() and then compute the similiarities and differences with a given student B and other dataset
    7. function4():
        a. First write all the books into a booklist.txt. (If the book exist in the txt file, it will not be written into it)
        b. Do a search on all the books without a genre
        c. return the search with the genre and then after that update the booklist file.
"""

import os

import AESCipher
import student_B as sb
import function2 as f2
import function4 as f4

CURENT_DIR = os.path.dirname(__file__)  # specify current directory
API_KEY_DIR = os.path.join(CURENT_DIR, "keys/")  # specify the keys directory
key_files = [file for file in os.listdir(API_KEY_DIR) if file.endswith(".bin")]  # list out the api-keys in keys folder
booklist_dir = CURENT_DIR + '/bookslist.txt'  # specify the booklist directory

"""
There will only be one file with one api key inside. In this use case, we will be using the already encrypted api key and store it in api-key.bin
1. First retrieve the API Key from api-key.bin
"""


def getAPIKey():  # retrieve the encrpyted API key
    api_dir = API_KEY_DIR + key_files[0]
    api_file = open(api_dir, "r")
    enc = api_file.read()
    api_file.close()

    return enc


class MAIN(object):
    def __init__(self, df):
        self.profiles_df = df

    def updateBooksGenre(self, password):
        aes = AESCipher  # calling the AES class
        enc = getAPIKey()  # getting the api key
        bk = f4.G_BOOKS(aes, enc, password)  # call the class G_Books in function to search for books

        # store all the books in the a text file
        bk.writeBooks2File(booklist_dir, self.profiles_df.Books.values)

        # open book file for reading
        book_file = open(booklist_dir, "r")
        line = book_file.read().splitlines()  # read file without \n

        # search of book genre starts here
        book_genre_dict = bk.get_book_genre(line)
        for key, value in book_genre_dict.iteritems():
            bk.update_file(booklist_dir, key, value)  # update the booklist.txt with books and its genre

        book_file.close()  # close the reading mode
        return bk

    def student_B(self, student_B_name):
        """ Getting student B information """
        student_B_info = sb.STUDENT_B(self.profiles_df)
        student_B_info = student_B_info.check_name(student_B_name)

        return student_B_info

    def function2(self, student_B_info, student_B_name):
        """ This part serves function 2 """
        f2_df = f2.COUNTRY_MATCH(self.profiles_df, student_B_name, student_B_info).countries_matches
        return f2_df

    def function3(self, f3_class, temp_profiles_list, student_B_info):
        count_likes = f3_class.countMatch(temp_profiles_list, student_B_info, "Likes")  # count the no. of likes
        count_dislikes = f3_class.countMatch(temp_profiles_list, student_B_info,
                                             "Dislikes")  # count the no. of dislikes

        f3_df = f3_class.matches(count_likes, count_dislikes, temp_profiles_list)  # get the final dataframe result
        # return tbe top 3 matches
        return f3_df.head(n=3)[
            ['Name', 'Gender', 'Country', 'Acceptable_country', 'Age', 'Acceptable_age_range', 'Likes',
             'Dislikes', 'Books', 'Birthday', "Rank"]]

    def function4(self, bk, temp_profiles_list, student_B_info):
        # Loading the updated list done by updateBookGenre(), converting into a dictionary
        bk_dict = {}
        with open(booklist_dir) as bk_file:
            for line in bk_file.read().splitlines():
                (key, value) = line.split("::")
                bk_dict[key] = value

        # Function 5 applys here to count the genre matches of student B with all the other students
        count_genre = bk.count_book_match(temp_profiles_list, student_B_info, bk_dict)
        f4_df = bk.matches(count_genre, temp_profiles_list)

        # return the top 3 results
        return f4_df.head(n=3)[
            ['Name', 'Gender', 'Country', 'Acceptable_country', 'Age', 'Acceptable_age_range', 'Likes',
             'Dislikes', 'Books', 'Birthday', "Rank"]]
