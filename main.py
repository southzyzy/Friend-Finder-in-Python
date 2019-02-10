import os
import sys
import time
import warnings
from multiprocessing import Process

import AESCipher
import student_B as sb
import function1 as f1
import function2 as f2
import function3 as f3
import function4 as f4

CURENT_DIR = os.path.dirname(__file__)  # specify current directory
PROFILES = os.path.join(CURENT_DIR, "profile/")  # locate the data profile
API_KEY_DIR = os.path.join(CURENT_DIR, "keys/")
pro_files = [file for file in os.listdir(PROFILES) if
             file.endswith(".txt")]  # list out all the profiles in profiles folder
key_files = [file for file in os.listdir(API_KEY_DIR) if file.endswith(".bin")]  # list out the api-keys in keys folder
booklist_dir = CURENT_DIR + '/bookslist.txt'


def updateBookGenre():
    aes = AESCipher
    api_dir = API_KEY_DIR + key_files[0]
    api_file = open(api_dir, "r")
    enc = api_file.read()
    api_file.close()

    book_file = open(booklist_dir, "r")
    line = book_file.read().splitlines()

    bk = f4.G_BOOKS(aes, enc, sys.argv[1])
    book_genre_dict = bk.get_book_genre(line)
    for key, value in book_genre_dict.iteritems():
        bk.updateFile(booklist_dir, key, value)

    book_file.close()


def main(student_B_name):
    warnings.filterwarnings('ignore')
    try:
        """ This part serves function 1 """
        profiles_list = f1.FUNCTION_1(profiles=PROFILES, files=pro_files)
        profiles_df = profiles_list.profilesDF(profiles_list.HEADERS, profiles_list.DATA)
        # store all the books in the a text file
        profiles_list.writeBooks2File(booklist_dir, profiles_df.Books.values)

        """ Getting student B information """
        student_B_info = sb.STUDENT_B(profiles_df)
        student_B_info = student_B_info.check_name(student_B_name)

        """ This part serves function 2 """
        f2_df = f2.COUNTRY_MATCH(profiles_df, student_B_name, student_B_info).countries_matches

        """ This part serves function 3 """
        f3_matches = f3.LIKES_DISLIKES(f2_df)  # calling the class LIKES_DISLIKES

        f3_matches_lst = f3_matches.temp_list  # converting dataframe to list

        countLikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Likes")  # count the no. of likes
        countDislikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Dislikes")  # count the no. of dislikes

        f3_df = f3_matches.matches(countLikes, countDislikes, f3_matches_lst)
        # print f3_df.head(n=3)[["Name", "Gender", "Rank"]]

    except Exception as e:
        print e


if __name__ == '__main__':
    start_time = time.time()
    student_B_name = "Joel Jackson"

    # main_process = Process(target=main, args=(student_B_name,))
    # main_process.start()

    # updatebook_process = Process(target=updateBookGenre)
    # updatebook_process.start()
    # updatebook_process.join()

    main(student_B_name)
    updateBookGenre()


    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))
    sys.exit()
