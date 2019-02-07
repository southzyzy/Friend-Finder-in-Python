class STUDENT_B(object):
    def __init__(self, df):
        self.df = df

    def check_name(self, name):
        if name in self.df.Name.values:
            return self.df.loc[self.df["Name"].isin([name])]

        else:
            print "No such user in the dataset!"
