class FUNCTION6(object):
    def __init__(self, final_df):
        self.df = final_df

    def convert2CSV(self, dir2Save, sb_name):
        self.df.to_csv(dir2Save + "/" + sb_name + "_matches.csv", index=None, header=True)
