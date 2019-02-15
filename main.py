import os

import AESCipher
import student_B as sb
import function2 as f2
import function4 as f4

CURENT_DIR = os.path.dirname(__file__)  # specify current directory
API_KEY_DIR = os.path.join(CURENT_DIR, "keys/")
key_files = [file for file in os.listdir(API_KEY_DIR) if file.endswith(".bin")]  # list out the api-keys in keys folder
booklist_dir = CURENT_DIR + '/bookslist.txt'


def getAPIKey():
    api_dir = API_KEY_DIR + key_files[0]
    api_file = open(api_dir, "r")
    enc = api_file.read()
    api_file.close()

    return enc


class MAIN(object):
    def __init__(self, df):
        self.profiles_df = df

    def updateBooksGenre(self, password):
        aes = AESCipher
        enc = getAPIKey()
        bk = f4.G_BOOKS(aes, enc, password)

        # store all the books in the a text file
        bk.writeBooks2File(booklist_dir, self.profiles_df.Books.values)

        book_file = open(booklist_dir, "r")
        line = book_file.read().splitlines()

        book_genre_dict = bk.get_book_genre(line)
        for key, value in book_genre_dict.iteritems():
            bk.update_file(booklist_dir, key, value)

        book_file.close()
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

        f3_df = f3_class.matches(count_likes, count_dislikes, temp_profiles_list)
        return f3_df.head(n=3)[
            ['Name', 'Gender', 'Country', 'Acceptable_country', 'Age', 'Acceptable_age_range', 'Likes',
             'Dislikes', 'Books', 'Birthday', "Rank"]]

    def function4(self, bk, temp_profiles_list, student_B_info):
        # Loading the updated list
        bk_dict = {}
        with open(booklist_dir) as bk_file:
            for line in bk_file.read().splitlines():
                (key, value) = line.split("::")
                bk_dict[key] = value

        count_genre = bk.count_book_match(temp_profiles_list, student_B_info, bk_dict)
        f4_df = bk.matches(count_genre, temp_profiles_list)
        return f4_df.head(n=3)[
            ['Name', 'Gender', 'Country', 'Acceptable_country', 'Age', 'Acceptable_age_range', 'Likes',
             'Dislikes', 'Books', 'Birthday', "Rank"]]