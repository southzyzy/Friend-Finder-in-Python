import pandas as pd
import function1 as f1
import function2 as f2
import function3 as f3

if __name__ == '__main__':
    """ This part serves function 1 """
    df_instances = f1.LOAD_PROFILES(f1.FILE_HANDLER().DATA, f1.FILE_HANDLER().HEADERS)
    df = df_instances.profilesDF

    """ This part serves function 2 """
    student_B = "Joel Jackson"
    countries_matches = f2.COUNTRY_MATCH(df, student_B).countries_matches


    """ This part serves function 3 """
    f3.LIKES(df, student_B, countries_matches)