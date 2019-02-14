import pandas as pd
import datetime as dt
import random
import horoscope as h
import calendar

class openFunction(object):
    def __init__(self, matched_profiles):
        # convert df object into a list
        self.profiles = list(matched_profiles.apply(
            lambda x: {
                "Name": x['Name'],
                "Gender": x["Gender"],
                "Country": x["Country"],
                "Acceptable_country": x["Acceptable_country"],
                "Age": x["Age"],
                "Acceptable_age_range": x["Acceptable_age_range"],
                "Likes": x['Likes'],
                "Books": x["Books"],
                "Dislikes": x['Dislikes'],
                "Birthday": x["Birthday"],
                "Rank": x['Rank']
            }, axis=1))

    # Generate choices
    def choiceGenerator(self):
        num = 1
        result = []
        # Create 3 choice statements
        while num < 4:
            standardAnswer = "%s"
            if num == 3:  # For a lower date range
                choice = standardAnswer % ((self.birthday - dt.timedelta(random.randint(1, 5))).strftime("%B %d"))
            elif num == 2:  # Correct answer template
                choice = standardAnswer % (self.birthday.strftime("%B %d"))
            else:  # For a higher date range
                choice = standardAnswer % ((self.birthday + dt.timedelta(random.randint(1, 5))).strftime("%B %d"))
            result.append(choice)
            num += 1
        result = random.sample(result,3) #randomize the choices
        return result

    # Obtain date range of horoscope (tuple data format)
    def tupleListDecoder(self, input):
        num = 1
        result = ""
        for x in input:
            result += "%d. %s\n" % (num, x)
            num += 1
        return result

    # Obtain the correct birthday answer via index number
    def getAnswer(self, input):
        correctDate = self.birthday.strftime("%B %d")
        for x in input:
            if x == correctDate:
                return (input.index(x) + 1)

    # Check if the birthday of the profile is even or odd
    def multipleCalculator(self):
        userBirthday = self.birthday
        day = userBirthday.day
        if day % 2 == 0:
            return "Even"
        else:
            return "Odd"

    #Create the range of birthday in 10 days apart, so as to give the user a rough guess.
    def birthdayRangeCalculator(self):
        birthdayLowerRange = self.birthday - dt.timedelta(5)
        birthdayUpperRange = self.birthday + dt.timedelta(5)
        range = birthdayLowerRange.strftime("%B %d") + " to " + birthdayUpperRange.strftime("%B %d")
        return range

    # Generate the string line statements for hints to the user on the correct profile birthday
    def birthdayHintGenerator(self):
        result = ""
        # Horoscope hint
        horoscope_range = h.Horoscope().get_horoscope_range(self.birthday)
        horoscope_range_string = ""
        for x in horoscope_range:
            horoscope_range_string += calendar.month_name[x[0]] + " " + str(x[1]) + " - "
        result += "We have a candidate here, with a Horoscope of %s" %(h.Horoscope().get_horoscope(self.birthday)) \
                  + " (%s)." % (horoscope_range_string[:-3]) + "\n"
        # Birthday range hint
        result += "Their birthday is in the range of %s" % (self.birthdayRangeCalculator()) + "\n"
        # Multiple of number hint
        result += "The day of their birthday is also a/an %s" % self.multipleCalculator() + " number."
        return result

    # Logical game method to obtain what to print for the start of the game (prints are in UI)
    def getGameIntro(self, profile):
        self.birthday = dt.datetime.strptime(profile[0]["Birthday"], "%Y-%m-%d").date()
        self.name = profile[0]["Name"]
        # First part: Introduction to the game
        introString = ""
        introString += "Welcome to Function 7 game!\n"
        introString += "We have selected a few candidates that you might like to view in this function...\n"
        introString += "However we think it is best that you get to know them a little more through a small game!\n"
        introString += "\n"
        # Second part: Hints for the profile guessing game
        hintString = self.birthdayHintGenerator()
        return introString + hintString

    #Start the multiple choice game
    def startGame(self,user_input,attempts,correctAnswer):
        # We will give the user 3 attempts for each candidate guess
        if not user_input.isdigit() or not 1 <= int(user_input) <= 3:
            return ["Please enter a valid answer! Choose a number from 1 to 3.",attempts]
        elif int(user_input) != correctAnswer:
            return ["Game: Wrong... Try again!",attempts-1]
        else:
            result = "\nYay you got it!!\n"
            result += "The instagram of this candidate is ------------------> @%s\n" %(self.name.lower())
            result += "Feel free to add him/her to start chatting!\n"
            return[result,0]
