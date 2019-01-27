import warnings
import function1 as f1
import function2 as f2
import function3 as f3

student_B = "Joel Jackson"

def function1():
    """ This part serves function 1 """
    df_instances = f1.LOAD_PROFILES(f1.FILE_HANDLER().DATA, f1.FILE_HANDLER().HEADERS)
    df = df_instances.profilesDF
    return df

def function2(df, student_B):
    """ This part serves function 2 """
    countries_matches = f2.COUNTRY_MATCH(df, student_B).countries_matches
    return countries_matches

def function3(df, student_B, countries_matches):
    """ This part serves function 3 """
    f3.LIKES(df, student_B, countries_matches)


def main():
    main_df = function1()
    country_df = function2(main_df, student_B)
    similarities_df = function3(main_df, student_B, country_df)


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    main()




