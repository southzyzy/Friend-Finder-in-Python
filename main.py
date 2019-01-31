import warnings, time
import function1 as f1
import function2 as f2
import function3 as f3
import student_B as sb


def function1():
    """ This part serves function 1 """
    df_instances = f1.PROFILES_DF(f1.FILE_HANDLER().DATA, f1.FILE_HANDLER().HEADERS)
    df = df_instances.profilesDF
    return df


def main():
    """ This part serves function 1 """
    main_df = function1()

    """ Getting student B information """
    student_B_name = "Tyesha Dicus"
    student_B_info = sb.STUDENT_B(main_df, student_B_name).student_B_info

    """ This part serves function 2 """
    f2_matches = f2.COUNTRY_MATCH(main_df, student_B_name, student_B_info).countries_matches

    """ This part serves function 3 """
    f3_matches = f3.LIKES_DISLIKES(f2_matches)
    f3_matches_lst = f3_matches.convert2List()
    countLikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Likes")
    countDislikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Dislikes")
    end = f3_matches.matches(countLikes, countDislikes, f3_matches_lst)
    print end


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start_time = time.time()
    main()
    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))
