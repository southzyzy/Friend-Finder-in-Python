class COUNTRY_MATCH:
    def __init__(self, df, name, student_B_info):
        student_B_gender = student_B_info.Gender.values[0]
        student_B_country = student_B_info["Acceptable_country"].values[0].split(", ")

        condition = df['Country'].isin(student_B_country) & (df['Name'] != name) & (df['Gender'] != student_B_gender)

        self.countries_matches = df.loc[condition]
        self.countries_matches["Rank"] +=1