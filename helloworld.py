import pandas as pd
import os, re
import multiprocessing as mp

path = "D:/SIT/ICT-1002 Programming Fundamentals/ICT1002_Tinder/profile/"


# filename = "D:/SIT/ICT-1002 Programming Fundamentals/Assignment/profile/1.txt"

def file_handler():
    files = [file for file in os.listdir(".\profile") if file.endswith(".txt")]

    HEADERS = ['Name', 'Gender', 'Country', 'Acceptable_country', 'Age', 'Acceptable_age_range', 'Likes', 'Dislikes',
               'Books']
    DATA = []

    for file in files:
        filename = path + file

        text_file = open(filename, "r")
        lines = text_file.read()
        text_file.close()

        books = re.search("(Name):(.*)\n+(Gender):(.*)\n+(Country):(.*)\n+(Acceptable_country):(.*)\n+(Age):(.*)\n+(Acceptable_age_range):(.*)\n+(Likes):(.*)\n+(Dislikes):(.*)\n+(Books):((?<=Books:)\D+)",lines)

        DATA.append([books.group(i).strip() for i in range(len(books.groups()) + 1) if not i % 2 and i != 0])

    df = pd.DataFrame(DATA, columns=HEADERS)
    df = df.replace('\n', ',', regex=True)
    # print df
    return df


def main():
    print "Hello World"


if __name__ == '__main__':
    file_handler()
