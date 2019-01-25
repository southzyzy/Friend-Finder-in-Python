import function1 as f1
import function2 as f2

if __name__ == '__main__':
    df_instances = f1.LOAD_PROFILES(f1.FILE_HANDLER().DATA, f1.FILE_HANDLER().HEADERS)
    df = df_instances.profilesDF
    matches = f2.COUNTRY_MATCH(df, "Michael Jackson")
    # print matches
