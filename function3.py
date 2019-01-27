class LIKES:
    def __init__(self, student_B_info, countries_matches):
        student_B_likes = student_B_info["Likes"].values[0].split(", ")
        student_B_dislikes = student_B_info["Dislikes"].values[0]

        a = countries_matches["Likes"].apply(lambda x : x)
        print a

        # matched = [df.loc[df["Name"] == n].apply(lambda x : (x["Name"], x["Likes"], x["Dislikes"]), axis=1) for n in matches_list_names]