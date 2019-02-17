"""
Function 2:
Pandas framework to extract all of the entire dataframe where it matches the student_B country.
    1. df['Country'].isin(student_B_country) -> iterate entire df and return the country that matches
    2. & operator to check if they are of the same gender, will not match same gender
    3. it will not match itself as well

Read More:
pandas.DataFrame.isin: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html
"""


class COUNTRY_MATCH:
    def __init__(self, df, name, student_B_info):
        student_B_gender = student_B_info.Gender.values[0]  # Get the selected student B gender

        student_B_country = student_B_info["Acceptable_country"].values[0].split(
            ",")  # Split the 'Acceptable_country' since its seperated with a ','

        # condition to match the above stated feature
        condition = df['Country'].isin(student_B_country) & (df['Name'] != name) & (df['Gender'] != student_B_gender)

        self.countries_matches = df.loc[condition]  # pass the condition to extract the matches
        self.countries_matches["Rank"] += 1.0  # create an extra column and add
