import pandas as pd
import warnings, time, os

from random import sample
from pyfiglet import Figlet
import cowsay
import progressbar as progressbar
from tabulate import tabulate

import main
import function1 as f1
import function3 as f3
import function6 as f6
import function7 as f7

CURENT_DIR = os.path.dirname(__file__)  # specify current directory
# PROFILES = os.path.join(CURENT_DIR, "profile/")  # locate the data profile
API_KEY_DIR = os.path.join(CURENT_DIR, "keys/")
key_files = [file for file in os.listdir(API_KEY_DIR) if file.endswith(".bin")]  # list out the api-keys in keys folder
booklist_dir = CURENT_DIR + '/bookslist.txt'

ERRMSG = {
    1: "Value Error! The option input is not provided in the function"
}


# Function to display the main menu
def display_ui():
    ui_banner = Figlet(font="graffiti")
    print ui_banner.renderText("Welcome To 1002_Tinder")
    cowsay.cow("Wanna Get Hitch? Use 1002_Tinder!")


def display_ui_2():
    cowsay.tux("User Profile Does Not Exist Within Our Database!")
    print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    print "Do You Wish To Display the Names of Students of a Specific Gender?"
    print "1. Display the Names of All Male Students."
    print "2. Display the Names of All Female Students."
    print "3. Return to Main Menu."
    print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"


def options_page():
    print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
    print "Options"
    print "1. List all the names, gender and age from all the profiles."
    print "2. List all the matched students of one given student B based on country."
    print "3. List the top 3 best matched students who share the most similar likes or dislikes for one given student B."
    print "4. List the top 3 best matched students based on books they like."
    print "5. List the top 3 best matched students based on the overall profile information which may include all the personal information for ranking."
    print "6. Store all the best matched students into one .csv file on the disk."
    print "7. Play the Function 7 birthday guessing game."
    print "8. Exit."
    print "9. Clear Screen (Enter 8 to clear screen)"
    print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="


# Main Program
def ui():
    """ This part serves function 1 """
    while True:
        profiles_dir = raw_input("Specify the profiles file directory => ")

        if not os.path.exists(profiles_dir):
            print 'Directory does not exist'
            continue

        elif [f for f in os.listdir(profiles_dir) if not f.startswith('.')] == []:
            print 'Profiles Directory specified is empty. Are you sure you point to the right directory?'
            continue

        else:
            profiles = [file for file in os.listdir(profiles_dir) if
                        file.endswith(".txt")]  # list out all the profiles in profiles folder
            break

    f1_list = f1.FUNCTION_1(profiles_dir=profiles_dir, files=profiles)
    df = f1_list.profilesDF(f1_list.HEADERS, f1_list.DATA)
    m_class = main.MAIN(df)

    # Variable to determine the state of the program
    program_exit = False

    while program_exit is not True:
        try:
            # Loads the option pages
            options_page()
            # Prompt the user to input his/her option
            choice = int(raw_input("What would you like to do => "))

        except ValueError:
            print ERRMSG.get(1)
            continue
        else:
            if choice < 0 or choice == 0 or choice > 9:
                print ERRMSG.get(1)
                continue

        # Option 1: List all the names, gender and age from all the profiles.
        if choice == 1:
            # Display the names, gender and age from all the profiles.
            print '\n'
            print (tabulate(m_class.profiles_df[
                                ['Name', 'Gender', 'Country', 'Acceptable_country', 'Age', 'Acceptable_age_range',
                                 'Likes', 'Dislikes']], headers='keys', tablefmt='psql'))
            print '\n'
            raw_input("Press Enter to return to main menu...")
            continue

        # Option 7: Exit.
        elif choice == 8:
            print "Thank You for Using 1002_Tinder!"
            print "Have a nice day!"
            program_exit = True

        elif choice == 9:
            os.system("cls")

        # Option 2 to Option 6
        else:
            while True:
                # Prompt the user to enter his/her profile name
                student_B_name = raw_input("Enter a profile name => ")

                """ This part get student B info """
                sb_df = m_class.student_B(student_B_name)

                if not isinstance(sb_df, pd.DataFrame):
                    display_ui_2()

                    while True:
                        try:
                            # Prompt the user to enter an input
                            sb_choice = int(raw_input("=> "))
                        except ValueError:
                            print ERRMSG.get(1)
                            continue
                        else:
                            break

                    if sb_choice == 0 or sb_choice > 3:
                        print ERRMSG.get(1)
                        continue
                    else:
                        # Option 1 to print out all the male in the dataset
                        if sb_choice == 1:
                            print '\n'
                            print(tabulate(
                                m_class.profiles_df[["Name", "Gender"]].loc[m_class.profiles_df['Gender'] == "M"],
                                headers='keys',
                                tablefmt='psql'))
                            print '\n'

                        # Option 2 to print out all the female in the dataset
                        elif sb_choice == 2:
                            print '\n'
                            print(tabulate(
                                m_class.profiles_df[["Name", "Gender"]].loc[m_class.profiles_df['Gender'] == "F"],
                                headers='keys',
                                tablefmt='psql'))
                            print '\n'

                        else:
                            break

                else:
                    try:
                        """ This part serves function 2 """
                        f2_df = m_class.function2(sb_df, student_B_name)

                        if choice == 2:
                            print '\n'
                            print(tabulate(f2_df[['Name', 'Gender', 'Country', 'Acceptable_country', 'Age',
                                                  'Acceptable_age_range', 'Likes', 'Dislikes', 'Rank']], headers='keys',
                                           tablefmt='psql'))
                            print '\n'
                            raw_input("Press Enter to return to main menu...")
                            break

                        """ This part serves function 3 """
                        f3_class = f3.LIKES_DISLIKES(f2_df)  # calling the class LIKES_DISLIKES
                        f3_temp_profiles_list = f3_class.temp_list  # converting dataframe to list

                        f3_df = m_class.function3(f3_class, f3_temp_profiles_list, sb_df)

                        if choice == 3:
                            print '\n'
                            print(tabulate(f3_df[['Name', 'Gender', 'Country', 'Acceptable_country', 'Age',
                                                  'Acceptable_age_range', 'Likes', 'Dislikes', 'Rank']], headers='keys',
                                           tablefmt='psql'))
                            print '\n'
                            raw_input("Press Enter to return to main menu...")
                            break

                        """ This part serves function 4 """

                        password = raw_input("Enter passphrase to decrypt API Eey => ")
                        bk = m_class.updateBooksGenre(password)

                        if choice == 4:
                            f4_class = f3.LIKES_DISLIKES(f2_df)  # calling the class LIKES_DISLIKES
                            f4_temp_profiles_list = f4_class.temp_list  # converting dataframe to list

                            f4_df = m_class.function4(bk, f4_temp_profiles_list, sb_df)

                            print '\n'
                            print(tabulate(f4_df[['Name', 'Gender', 'Rank']], headers='keys',
                                           tablefmt='psql'))
                            print '\n'
                            raw_input("Press Enter to return to main menu...")
                            break

                        """ This part serves function 5 """
                        f5_df = m_class.function4(bk, f3_temp_profiles_list, sb_df)
                        if choice == 5:
                            print '\n'
                            print(tabulate(f5_df[['Name', 'Gender', 'Country', 'Acceptable_country', 'Age',
                                                  'Acceptable_age_range', 'Likes', 'Dislikes', 'Rank']], headers='keys',
                                           tablefmt='psql'))
                            print '\n'
                            raw_input("Press Enter to return to main menu...")
                            break

                        """ This part serves function 6 """
                        if choice == 6:

                            print '\n'
                            bar = progressbar.ProgressBar(maxval=20, widgets=['Converting to CSV ... ',
                                                                              progressbar.Bar('=', '[', ']'), ' ',
                                                                              progressbar.Percentage()])
                            bar.start()
                            for i in xrange(20):
                                bar.update(i + 1)
                                time.sleep(0.1)

                            f6_class = f6.FUNCTION6(f5_df)
                            f6_class.convert2CSV(CURENT_DIR, student_B_name)

                            bar.finish()

                            print '\n'

                            raw_input("Press Enter to return to main menu...")
                            break

                        else:
                            """This part serves function 7"""
                            # Initialize function 7 and get a list of matched profiles
                            print '\n'
                            print '-------------------------------------------------------------------------------------'
                            print 'HELLO %s !' % student_B_name.upper(),
                            game = f7.openFunction(f5_df)
                            exclude_profile = []  # This is for excluding profiles that have done the game
                            count = 0
                            while count < len(game.profiles):
                                # Randomly select a profile that has not been used for the game
                                random_profile = sample([i for i in game.profiles if i not in exclude_profile],
                                                        1)
                                # Add the selected profile into the exclude list
                                exclude_profile.append(random_profile[0])
                                count += 1
                                print game.getGameIntro(random_profile)  # Print intro + hints
                                choices = game.choiceGenerator()
                                correctAnswer = game.getAnswer(choices)
                                print game.tupleListDecoder(choices)  # Print multiple choices
                                attempts = 3
                                while attempts > 0:
                                    user_input = raw_input("What is their birthday?(Select by number, i.e 1!) => ")
                                    gameData = game.startGame(user_input, attempts,
                                                              correctAnswer)  # Printstring[0], attempt number[1]
                                    print gameData[0]
                                    attempts = gameData[1]
                                while True:
                                    # Ask player if they wish to guess another candidate.
                                    answer = raw_input(
                                        "Would you like to guess another one of your top few most matched candidate? (Y/N) => ")
                                    if answer.lower() == "n":
                                        print "Thanks for playing, see you next time!"
                                        count = len(game.profiles)  # Break the profile selection loop
                                        break
                                    elif answer.lower() == "y":
                                        # Stop the game when all of the profiles available are visited
                                        if count == len(game.profiles):
                                            print "Sorry, looks like you have reached the end of your most matched candidates, thanks for playing!"
                                        break
                                    else:
                                        # Invalid values
                                        print "Please enter Y or N!"

                            print '\n'
                            raw_input("Press Enter to return to main menu...")
                            break

                    except Exception as e:
                        print e
                        break


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start_time = time.time()
    # Display banner & Options
    display_ui()
    ui()
    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))
