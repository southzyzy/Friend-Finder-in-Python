class COUNTRY_MATCH:
    def __init__(self, df, name):
        student_B_info = df.loc[df["Name"].isin([name])]
        student_B_gender = student_B_info.Gender.str
        student_B_country = student_B_info["Acceptable_country"].values[0].split(", ")
        condition = df['Country'].isin(student_B_country) & (df['Name'] != name) & (df['Gender'] != student_B_gender)
        self.countries_matches = df.loc[condition].apply(lambda x : (x["Name"], x['Gender'], x['Country'], x['Rank']+1), axis=1)