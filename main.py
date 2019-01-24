import file_handler as fh


if __name__ == '__main__':
    df = fh.LOAD_PROFILES(fh.FILE_HANDLER().DATA, fh.FILE_HANDLER().HEADERS)
    print df.profilesDF
