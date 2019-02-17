"""
Student_B:
Iterate all the dataset and attempts to determine if Student B exists within the dataset

More Info:
pandas.DataFrame.loc: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
"""

class STUDENT_B(object):
    def __init__(self, df):
        self.df = df

    def check_name(self, name):
        name = name.lower() # change the input name into lower case
        if name in map(lambda x: x.lower(), self.df.Name.values): # do the checking to see if the name exist in the dataframe
            return self.df.loc[self.df.Name.str.lower().isin([name])] # if exist, return the dataframe of studnent B


        else:
            return "Error" # if not, return an error to output the error message
