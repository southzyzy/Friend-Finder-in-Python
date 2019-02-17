"""
Function 3:
Author: @ Jerome
Function 5 Ranking Metric: Kish & Koh Jie

Iterate all the dataset and find the similarities and differences of every other student with student B Likes and Dislikes.
    1. Convert dataframe into a list with .apply(lambda)
    2. Function 5 implemented here with the counting of the amt of likes and dislikes @ countMatch()
    3. Updating the dataframe by adding the final score to it

Read More:
pandas.DataFrame.apply: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
"""

import pandas as pd


class LIKES_DISLIKES(object):
    def __init__(self, df):
        # convert df object to a list
        self.temp_list = list(df.apply(
            lambda x: {
                "Name": x['Name'],
                "Gender": x["Gender"],
                "Country": x["Country"],
                "Acceptable_country": x["Acceptable_country"],
                "Age": x["Age"],
                "Acceptable_age_range": x["Acceptable_age_range"],
                "Likes": x['Likes'],
                "Dislikes": x['Dislikes'],
                "Books": x["Books"],
                "Birthday": x["Birthday"],
                "Rank": x['Rank']
            }, axis=1))

    # This Part is where the function 5 is. COUNTING OF THE RANKING METRIC
    def countMatch(self, temp_list, sb_info, term):
        """
            ### Counting Likes and Dislikes
            1. if student B likes and matched likes same == +1
            2. if student B dislikes and matched dislikes same == +1
            3. if student B like smth and matched dislike same as the B_like == -0.5
            4. if student B dislike smth and matched like same as the B_dislike == -0.5
         """
        similarities_list = sb_info[term].values[0].split(",")

        count = 0
        d = {}

        for i in temp_list:
            for val in similarities_list:
                for a in i[term].split(","):
                    if val in a:
                        count += 1.0

                if term == "Likes":  # 3. if student B like smth and matched dislike same as the B_like == -0.5
                    for _ in i["Dislikes"].split(","):
                        if val in _:
                            count -= 0.5
                else:  # if student B dislike smth and matched like same as the B_dislike == -0.5
                    for _ in i["Likes"].split(","):
                        if val in _:
                            count -= 0.5

            d[i["Name"]] = count
            count = 0  # reset count to 0

        return d

    def matches(self, count_likes, count_dislikes, temp_list):
        for i in temp_list:
            i["Rank"] += count_likes.get(i["Name"])
            i["Rank"] += count_dislikes.get(i["Name"])

        f3_df = pd.DataFrame.from_dict(temp_list, orient='columns')
        return f3_df.sort_values(by=["Rank"], ascending=False)
