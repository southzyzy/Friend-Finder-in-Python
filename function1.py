"""
Function 1:
Author: @ Ryan Goh

Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
    1. Use of regex expression to filter and extract the data
    2. Pass the data and convert data into a pandas dataframe
    3. Format the dataframe to remove any error for data handling

Read More:
pandas: https://pandas.pydata.org/
"""

import pandas as pd
import re


# Part 3
def formattingData(df):
    # Check Gender column
    df["Gender"] = df.Gender.str.replace("Female", "F")  # Replace all 'Female' to 'F'
    df["Gender"] = df.Gender.str.replace("Male", "M")  # Replace all 'Male' to 'M'

    df["Acceptable_country"] = df.Acceptable_country.str.replace(", ", ",")  # remove the white space after ,
    df["Likes"] = df.Likes.str.replace(", ", ",")  # remove white spaces after ,
    df["Dislikes"] = df.Dislikes.str.replace(", ", ",")  # remove white spaces after ,
    df = df.replace('\n', '|', regex=True)  # replace all the \n in Books to ','

    return df


class FUNCTION_1(object):
    def __init__(self, profiles_dir, files):
        # specify the column header
        self.HEADERS = ['Name', 'Gender', 'Country', 'Acceptable_country', 'Age', 'Acceptable_age_range', 'Likes',
                        'Dislikes', 'Books', 'Birthday']

        self.DATA = []  # create the empty list to store profiles

        for file in files:  # iterate over each file
            filename = profiles_dir + '/' + file  # full path name of the data files

            text_file = open(filename, "r")  # open the file
            lines = text_file.read()  # read the file in memory
            text_file.close()  # close the file

            """
            Regex to filter out all the column header and row data. 
            Odd Number == Header, Even Number == Data
            """
            profiles_data = re.search(
                "(Name):(.*)\n+(Gender):(.*)\n+(Country):(.*)\n+(Acceptable_country):(.*)\n+(Age):(.*)\n+(Acceptable_age_range):(.*)\n+(Likes):(.*)\n+(Dislikes):(.*)\n+(Books):((?<=Books:)\D+)\n+(Birthday):(.*)",
                lines)

            # append data into DATA list
            self.DATA.append([profiles_data.group(i).strip() for i in range(len(profiles_data.groups()) + 1) if
                              not i % 2 and i != 0])

    def profilesDF(self, headers, data):
        df = pd.DataFrame(data, columns=headers)  # create the dataframe
        df = formattingData(df)  # format and make data nicer
        df["Rank"] = 0.0  # create a column Rank to rank the matches
        return df
