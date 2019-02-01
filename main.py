import warnings, time, os
# import function1 as f1
import function1 as f1
import function2 as f2
import function3 as f3
import student_B as sb

CURENT_DIR = os.path.dirname(__file__)  # specify current directory
PROFILES = os.path.join(CURENT_DIR, "profile/")  # locate the data profile
files = [file for file in os.listdir(PROFILES) if file.endswith(".txt")]  # list out all the filename in profiles folder


def main():
    """ This part serves function 1 """
    profiles_list = f1.FUNCTION_1(profiles=PROFILES, files=files)
    profiles_df = profiles_list.profilesDF(profiles_list.HEADERS, profiles_list.DATA)

    """ Getting student B information """
    student_B_name = "Tyesha Dicus"
    student_B_info = sb.STUDENT_B(profiles_df, student_B_name).student_B_info

    """ This part serves function 2 """
    f2_matches = f2.COUNTRY_MATCH(profiles_df, student_B_name, student_B_info).countries_matches

    """ This part serves function 3 """
    f3_matches = f3.LIKES_DISLIKES(f2_matches)  # calling the class LIKES_DISLIKES
    f3_matches_lst = f3_matches.convert2List()  # converting dataframe to list
    countLikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Likes")  # count the no. of likes
    countDislikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Dislikes")  # count the no. of dislikes
    end = f3_matches.matches(countLikes, countDislikes, f3_matches_lst)
    print end


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start_time = time.time()
    main()
    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))
