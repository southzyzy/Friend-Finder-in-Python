import pandas as pd


def countMatch(temp_list, lst, term):
    # get the likes or dislikes list
    similarities_list = lst[term].values[0].split(",")

    count = 0
    d = {}

    for i in temp_list:
        for val in similarities_list:
            for a in i[term].split(","):
                if val in a:
                    count += 1
        d[i["Name"]] = count
        count = 0  # reset count to 0
    return d

# def countNotMatch(temp_list, lst, term):
#
#


class CONVERT_TO_LIST:
    def __init__(self, f2_matches):
        # convert df object to a list
        self.temp_list = list(f2_matches.apply(
            lambda x: {
                "Name": x['Name'],
                "Likes": x['Likes'],
                "Dislikes": x['Dislikes'],
                "Rank": x['Rank'],
            }, axis=1))


class LIKES_DISLIKES:
    def __init__(self, student_B_info, temp_list):
        """ 
            ### Counting Likes and Dislikes
            1. if student B likes and matched likes same == +1
            2. if student B dislikes and matched dislikes same == +1
            3. if student B like smth and matched dislike same as the B_like == -0.5
            4. if student B dislike smth and matched like same as the B_dislike == -0.5
         """
        countLikes = countMatch(temp_list, student_B_info, "Likes")
        countDislikes = countMatch(temp_list, student_B_info, "Dislikes")


        for i in temp_list:
            i["Rank"] += countLikes.get(i["Name"])
            i["Rank"] += countDislikes.get(i["Name"])

        print pd.DataFrame.from_dict(temp_list)







