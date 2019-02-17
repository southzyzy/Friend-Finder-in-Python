"""
Student_B:
Iterate all the dataset and attempts to determine if Student B exists within the dataset 
"""

class STUDENT_B(object):
    def __init__(self, df):
        self.df = df

    def check_name(self, name):
        name = name.lower()
        if name in map(lambda x: x.lower(), self.df.Name.values):
            return self.df.loc[self.df.Name.str.lower().isin([name])]


        else:
            return "Error"
