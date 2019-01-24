import pandas as pd
import os, re

CURENT_DIR = os.path.dirname(__file__)
PROFILES = os.path.join(CURENT_DIR, "profile/")
files = [file for file in os.listdir(PROFILES) if file.endswith(".txt")]


class FILE_HANDLER:
    def __init__(self):
        self.DATA = []

        for file in files:
            filename = PROFILES + file

            text_file = open(filename, "r")
            lines = text_file.read()
            text_file.close()

            books = re.search(
                "(Name):(.*)\n+(Gender):(.*)\n+(Country):(.*)\n+(Acceptable_country):(.*)\n+(Age):(.*)\n+(Acceptable_age_range):(.*)\n+(Likes):(.*)\n+(Dislikes):(.*)\n+(Books):((?<=Books:)\D+)",
                lines)

            self.DATA.append([books.group(i).strip() for i in range(len(books.groups()) + 1) if not i % 2 and i != 0])

            self.HEADERS = ['Name', 'Gender', 'Country', 'Acceptable_country', 'Age', 'Acceptable_age_range', 'Likes',
                            'Dislikes', 'Books']


class LOAD_PROFILES:
    def __init__(self, data, headers):
        self.profilesDF = pd.DataFrame(data, columns=headers)
        self.profilesDF = self.profilesDF.replace('\n', ',', regex=True)
