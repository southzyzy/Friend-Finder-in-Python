import os
import sys
import time
import warnings
from multiprocessing import Process, Queue, Pool
from multiprocessing.managers import BaseManager

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


def main():
    try:
        """ This part serves function 1 """
        profiles_list = f1.FUNCTION_1(profiles=PROFILES, files=pro_files)
        profiles_df = profiles_list.profilesDF(profiles_list.HEADERS, profiles_list.DATA)

        """ Getting student B information """
        student_B_name = "Joel Jackson"
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
        print f3_df.head(n=3)[["Name", "Gender", "Rank"]]

        """ This part serves function 4 """
        aes = AESCipher
        api_dir = "D:/SIT/ICT-1002 Programming Fundamentals/ICT1002_Tinder\keys/api-key.txt.bin"
        api_file = open(api_dir, "r")
        enc = api_file.read()
        api_file.close()

        bk = f4.G_BOOKS(aes, enc, sys.argv[1])
        for book in student_B_info.Books.values:
            for _ in book.split(","):
                result = bk.search(_.rstrip())

        print result

    except Exception as e:
        print e


if __name__ == '__main__':
    start_time = time.time()
    warnings.filterwarnings('ignore')
    main()
    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))
