class LIKES:
    def __init__(self, df, name, countries_matches):
        matches_list_names = [countries_matches.values[i][0] for i in range(len(countries_matches))]
        matched_df = df.loc[df["Name"].isin(matches_list_names)]


        # matched = [df.loc[df["Name"] == n].apply(lambda x : (x["Name"], x["Likes"], x["Dislikes"]), axis=1) for n in matches_list_names]
        # likes = [single_match.values[0][1].split(", ") for single_match in matched]
        # dislikes = [single_match.values[0][2].split(", ") for single_match in matched]

        # condition = df['Likes'].isin(likes) & (df['Name'] != name)
        # print condition



        # student_B_gender = student_B.values[0][1]
        # student_B_country = student_B.values[0][2].split(", ")
        # condition = df['Country'].isin(student_B_country) & (df['Name'] != name) & (df['Gender'] != student_B_gender)
        # self.matched = df.loc[condition].apply(lambda x : (x["Name"], x['Gender'], x['Country'], x['Rank']+1), axis=1)