"""
Function 6:
    1. Uses Pandas's built-in .DataFrame.to_csv method to export data from the dataframe to a .csv file 

Read More:
pandas.DataFrame.apply: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
"""




class FUNCTION6(object):
    def __init__(self, final_df):
        self.df = final_df

    def convert2CSV(self, dir2Save, sb_name):
        self.df.to_csv(dir2Save + "/" + sb_name + "_matches.csv", index=None, header=True)
