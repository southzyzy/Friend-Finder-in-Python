from pyfiglet import Figlet
import cowsay
import warnings, time, os
import function1 as f1
import function2 as f2
import function3 as f3
import student_B as sb

CURENT_DIR = os.path.dirname(__file__)  # specify current directory
PROFILES = os.path.join(CURENT_DIR, "profile/")  # locate the data profile
files = [file for file in os.listdir(PROFILES) if file.endswith(".txt")]  # list out all the filename in profiles folder


def display_ui():
    ui_banner = Figlet(font="graffiti")
    print ui_banner.renderText("Welcome To 1002_Tinder")
    cowsay.cow("Wanna Get Hitch? Use 1002_Tinder!")

    print "1. List all the names, gender and age from all the profiles."
    print "2. List all the matched students of one given student B based on country."
    print "3. List the top 3 best matched students who share the most similar likes or dislikes for one given student B."
    print "4. List the top 3 best matched students based on books they like."
    print "5. List the top 3 best matched students based on the overall profile information which may include all the personal information for ranking."
    print "6. Store all the best matched students into one .csv file on the disk."
    print "7. Exit. \n"


def main():
    profiles_list = f1.FUNCTION_1(profiles=PROFILES, files=files)
    profiles_df = profiles_list.profilesDF(profiles_list.HEADERS, profiles_list.DATA)

    acceptable_inputs = ["1", "2", "3", "4", "5", "6", "7"]
    display_ui()

    # Getting student B information
    user_profile_path = raw_input("Please Import Your Profile Here: ")

    student_B_name = "Kevin"
    student_B_info = sb.STUDENT_B(profiles_df, student_B_name).student_B_info

    # Getting user to input his/her option
    user_input = raw_input("Enter your option: ")

    # User entered a valid input
    if user_input in acceptable_inputs:

        while user_input in acceptable_inputs:

            """Put this here"""
            profiles_list = f1.FUNCTION_1(profiles=PROFILES, files=files)
            profiles_df = profiles_list.profilesDF(profiles_list.HEADERS, profiles_list.DATA)

            # Option 1
            if user_input == "1":
                print profiles_df
                print "\n \n \n \n"

                display_ui()
                user_input = raw_input("Enter your option: ")


            # Option 2
            elif user_input == "2":
                f2_df = f2.COUNTRY_MATCH(profiles_df, student_B_name, student_B_info).countries_matches

                print f2_df
                print "\n \n \n \n"

                display_ui()
                user_input = raw_input("Enter your option: ")


            # Option 3

            # Option 7
            elif user_input == "7":
                print "Thank You for Using 1002_Tinder!"
                print "Have a nice day!"
                break

                # User entered an invalid input
    else:
        print "Invalid Option Entered! Exiting Program."
        print "Thank You for Using 1002_Tinder!"


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start_time = time.time()
    main()
    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))






