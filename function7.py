import pandas as pd
import datetime as dt
import random

#To do top few candidates retrevial here
#Example data usage here (to be replaced)
name = "Lane"
gender = "Female"
country = "Singapore"
acceptable_country = "Singapore"
age = "21"
acceptable_age_range = "20-30"
likes = "ice cream, tom yum, books, flowers"
dislikes = "insects, sports, dirt"
books = "Harry potter, Code black, the dark behind the curtain"
birthday = "1998-5-24"
horoscope = "Cancer"
instrgram = "@mehere"
#Example data usage here (to be replaced)

#def horoscopeDefiner(date):
    #dt.datetime.strptime(birthday, "%Y-%m-%d").date()
    #Example of the horoscope calcuation

#Create the range of birthday in 10 days apart, so as to give the user a rough guess.
def birthdayRangeCalculator(birthday):
    birthday = dt.datetime.strptime(birthday, "%Y-%m-%d").date()
    birthdayLowerRange = birthday - dt.timedelta(5)
    birthdayUpperRange = birthday + dt.timedelta(5)
    range = birthdayLowerRange.strftime("%B %d") + " to " + birthdayUpperRange.strftime("%B %d")
    return range

#Generate choices
def choiceGenerator(birthday):
    userBirthday = dt.datetime.strptime(birthday, "%Y-%m-%d").date()
    num = 1;
    result = [];
    #Create 3 choice statements
    while num < 4:
        standardAnswer = "%s"
        if num == 3: #For a lower date range
            choice = standardAnswer %((userBirthday - dt.timedelta(random.randint(1,5))).strftime("%B %d"))
        elif num == 2: #Correct answer template
            choice = standardAnswer % (userBirthday.strftime("%B %d"))
        else: #For a higher date range
            choice = standardAnswer % ((userBirthday + dt.timedelta(random.randint(1, 5))).strftime("%B %d"))
        result.append(choice)
        num += 1;
    return result

def multipleCalculator(birthday):
    userBirthday = dt.datetime.strptime(birthday,"%Y-%m-%d").date()
    day = userBirthday.day;
    if day % 2 == 0:
        return "Even"
    else:
        return "Odd"

def startGame():
    print "Welcome to Function 7 game!"
    print "We have selected a few candidates that you might like to view in this function..."
    print "However we think it is best that you get to know them a little more through a small game!"
    print " "
    #Horoscope hint
    print "We have a candidate here, with a Horoscope of %s" % (horoscope) + " (Jun 21 - Jul 23)."
    #Birthday range hint
    print "Their birthday is in the range of %s" %(birthdayRangeCalculator(birthday))
    #Multiple of number hint
    print "The day of their birthday is also a/an %s" %multipleCalculator(birthday) + " number"
    #Obtain the three multiple choices that the user can pick. Note that the answer is true string answer.
    choices = choiceGenerator(birthday)
    correctChoice = choices[1] #Predefined correct answer before reshuffling the choice deck
    shuffledChoice = random.sample(choices, 3) #Randomized answer list based on using random sampling
    #Print multiple choices for user to choose
    for x in shuffledChoice:
        print x
    #We will give the user 3 attempts for each candidate guess
    attempts = 3
    while attempts > 0:
        user_input = raw_input("What is their birthday?: ")
        if user_input != correctChoice:
            print "Game: Wrong... Try again!"
            attempts -= 1 #Wrong selection
        else:
            print "Yay you got it!!"
            print "The instagram of this candidate is: " + instrgram #requires instagram data
            print "Feel free to add him/her to start chatting!"
            attempts = 0;
    print "---"
    #Ask player if they wish to guess another candidate. Limit to the number of available candidates (5 people likely)
    answer = raw_input("Would you like to guess another one of your top few most matched candidate (Y/N)?:")
