class FUNCTION6(object):
    def __init__(self, final_df):
        self.df = final_df

    def convert2CSV(self):
        self.df.to_csv("function6.csv", index=None, header=True)
