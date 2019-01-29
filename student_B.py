class STUDENT_B:
    def __init__(self, df, name):
        self.student_B_info = df.loc[df["Name"].isin([name])]
        print self.student_B_info[["Name","Likes"]]