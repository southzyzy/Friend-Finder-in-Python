import pandas as pd
import os, re

CURENT_DIR = os.path.dirname(__file__)  # specify current directory
PROFILES = os.path.join(CURENT_DIR, "profile/")  # locate the data profile
files = [file for file in os.listdir(PROFILES) if file.endswith(".txt")]  # list out all the filename in profiles folder


def formattingData(df):
    # replace F to Female
    # print df.Gender.str.contains("F")
    df["Gender"] = df.Gender.str.replace("F", "Female")
    df["Acceptable_country"] = df.Acceptable_country.str.replace(", ", ",")  # remove the white space after ,
    df["Likes"] = df.Likes.str.replace(", ", ",")  # remove white spaces after ,
    df["Dislikes"] = df.Dislikes.str.replace(", ", ",")  # remove white spaces after ,
    df = df.replace('\n', ',', regex=True)  # replace all the \n in Books to ','
    return df


class FILE_HANDLER:
    def __init__(self):
        # specify the column header
        self.HEADERS = ['Name', 'Gender', 'Country', 'Acceptable_country', 'Age', 'Acceptable_age_range', 'Likes',
                        'Dislikes', 'Books']

        self.DATA = []  # create the empty list to store profiles

        for file in files:  # iterate over each file
            filename = PROFILES + file  # full path name of the data files

            text_file = open(filename, "r")  # open the file
            lines = text_file.read()  # read the file in memory
            text_file.close()  # close the file

            """
            Regex to filter out all the column header and row data. 
            Odd Number == Header, Even Number == Data
            """
            profiles_data = re.search(
                "(Name):(.*)\n+(Gender):(.*)\n+(Country):(.*)\n+(Acceptable_country):(.*)\n+(Age):(.*)\n+(Acceptable_age_range):(.*)\n+(Likes):(.*)\n+(Dislikes):(.*)\n+(Books):((?<=Books:)\D+)",
                lines)

            # append data into DATA list
            self.DATA.append([profiles_data.group(i).strip() for i in range(len(profiles_data.groups()) + 1) if
                              not i % 2 and i != 0])


class PROFILES_DF:
    def __init__(self, data, headers):
        self.profilesDF = pd.DataFrame(data, columns=headers)  # create the dataframe
        self.profilesDF = formattingData(self.profilesDF)  # format and make data nicer
        self.profilesDF["Rank"] = 0.0  # create a column Rank to rank the matches
