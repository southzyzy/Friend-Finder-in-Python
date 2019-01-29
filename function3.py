def countMatch(likes_list, student_B_likes):
    count = 0
    count_list = []

    for i in likes_list:
        for val in student_B_likes:
            if val in i:
                count+=1
        count_list.append(count)
    return count_list



class LIKES_DISLIKES:
    def __init__(self, student_B_info, f2_matches):
        student_B_likes = student_B_info["Likes"].values[0].split(",")
        student_B_dislikes = student_B_info["Dislikes"].values[0].split(",")

        d = {}

        likes_list = [f2_matches["Likes"].values[i].split(",") for i in range(len(f2_matches))]
        a = countMatch(likes_list, student_B_likes)
        print a

        # a = [(lambda x : x["Likes"])(x) for x in temp_list]

        # student_B = lambda x : (x["Name"], x["Acceptable_country"])
        # matched = filter(lambda i : i ==  student_B(d[1])[1], map(lambda x : (x[1]["Acceptable_country"]), d.iteritems()))

        # matched = [df.loc[df["Name"] == n].apply(lambda x : (x["Name"], x["Likes"], x["Dislikes"]), axis=1) for n in matches_list_names]
