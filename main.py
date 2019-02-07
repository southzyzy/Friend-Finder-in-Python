import os
import sys
import time
import warnings
from multiprocessing import Process, Queue

import AESCipher
import student_B as sb
import function1 as f1
import function2 as f2
import function3 as f3
import function4 as f4

CURENT_DIR = os.path.dirname(__file__)  # specify current directory
PROFILES = os.path.join(CURENT_DIR, "profile/")  # locate the data profile
API_KEY = os.path.join(CURENT_DIR, "keys/")
pro_files = [file for file in os.listdir(PROFILES) if
             file.endswith(".txt")]  # list out all the profiles in profiles folder
key_files = [file for file in os.listdir(API_KEY) if file.endswith(".bin")]  # list out the api-keys in keys folder



def function1(f1q):
    """ This part serves function 1 """
    profiles_list = f1.FUNCTION_1(profiles=PROFILES, files=pro_files)
    profiles_df = profiles_list.profilesDF(profiles_list.HEADERS, profiles_list.DATA)
    f1q.put(profiles_df)


def function4(sbq, f4q):
    """ This part serves function 4 """
    aes = AESCipher
    api_dir = "D:/SIT/ICT-1002 Programming Fundamentals/ICT1002_Tinder\keys/api-key.txt.bin"
    api_file = open(api_dir, "r")
    enc = api_file.read()
    api_file.close()

    student_B_info = sbq.get()

    bk = f4.G_BOOKS(aes, enc, sys.argv[1])
    for book in student_B_info.Books.values:
        for _ in book.split("|"):
            result = bk.search(_.rstrip())

    genre_list = bk.compareBooks(result, student_B_info)
    f4q.put(genre_list)


def main(f1q, sbq, student_B_name, f4q):
    try:
        profiles_df = f1q.get()

        """ Getting student B information """
        student_B_info = sb.STUDENT_B(profiles_df)
        student_B_info = student_B_info.check_name(student_B_name)
        sbq.put(student_B_info)

        """ This part serves function 2 """
        f2_df = f2.COUNTRY_MATCH(profiles_df, student_B_name, student_B_info).countries_matches

        """ This part serves function 3 """
        f3_matches = f3.LIKES_DISLIKES(f2_df)  # calling the class LIKES_DISLIKES

        f3_matches_lst = f3_matches.temp_list  # converting dataframe to list

        countLikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Likes")  # count the no. of likes
        countDislikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Dislikes")  # count the no. of dislikes

        f3_df = f3_matches.matches(countLikes, countDislikes, f3_matches_lst)
        print f3_df.head(n=3)[["Name", "Gender", "Rank"]]


        """ Function 4 Starts here """
        sb_genre = f4q.get()
        print sb_genre


    except Exception as e:
        print e


if __name__ == '__main__':
    warnings.filterwarnings('ignore')

    start_time = time.time()
    student_B_name = "Joel Jackson"

    f1q = Queue()
    sbq = Queue()
    f4q = Queue()

    f4_process = Process(target=function4, args=(sbq, f4q))
    f4_process.start()

    f1_process = Process(target=function1, args=(f1q,))
    f1_process.start()

    main_process = Process(target=main, args=(f1q, sbq, student_B_name, f4q))
    main_process.start()
    f4_process.join()

    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))
    sys.exit()
