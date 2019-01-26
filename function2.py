import pandas as pd

class COUNTRY_MATCH:
    def __init__(self, df, name):
        student_B = df.loc[df["Name"] == name].apply(lambda x : (x["Gender"], x['Acceptable_country']), axis=1)
        countries = df.loc[df['Country'].isin(student_B[0][1].split(", ")) & (df['Name'] != name) & (df['Gender'] != student_B[0][0])].apply(lambda x : (x["Name"], x['Gender'], x['Country']), axis=1)
        print countries


