import warnings
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
    # Function 1
    main_df = function1()

    # Getting student B information
    student_B_name = "Son Spanbauer"
    student_B_info = sb.STUDENT_B(main_df, student_B_name).student_B_info

    """ This part serves function 2 """
    f2_matches = f2.COUNTRY_MATCH(main_df, student_B_name, student_B_info).countries_matches

    """ This part serves function 3 """
    f3_matches = f3.LIKES_DISLIKES(student_B_info, f3.CONVERT_TO_LIST(f2_matches).temp_list).f3_df
    print f3_matches[["Name","Rank"]]


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    main()
