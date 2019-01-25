import function1 as f1


if __name__ == '__main__':
    df = f1.LOAD_PROFILES(f1.FILE_HANDLER().DATA, f1.FILE_HANDLER().HEADERS)
    print df.profilesDF["Books"]
