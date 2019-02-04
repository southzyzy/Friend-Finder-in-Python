from pyfiglet import Figlet
import cowsay
import sys
import warnings, time, os
import function1 as f1
import function2 as f2
import function3 as f3
import student_B as sb

CURENT_DIR = os.path.dirname(__file__)  # specify current directory
PROFILES = os.path.join(CURENT_DIR, "profile/")  # locate the data profile
API_KEY = os.path.join(CURENT_DIR, "keys/")
pro_files = [file for file in os.listdir(PROFILES) if
             file.endswith(".txt")]  # list out all the profiles in profiles folder
key_files = [file for file in os.listdir(API_KEY) if file.endswith(".bin")]  # list out the api-keys in keys folder


def display_ui():
    ui_banner = Figlet(font = "graffiti")
    print ui_banner.renderText("Welcome To 1002_Tinder")
    cowsay.cow("Wanna Get Hitch? Use 1002_Tinder!")

def options():
    print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
    print "Options"
    print "1. List all the names, gender and age from all the profiles."
    print "2. List all the matched students of one given student B based on country."
    print "3. List the top 3 best matched students who share the most similar likes or dislikes for one given student B."
    print "4. List the top 3 best matched students based on books they like."
    print "5. List the top 3 best matched students based on the overall profile information which may include all the personal information for ranking."
    print "6. Store all the best matched students into one .csv file on the disk."
    print "7. Exit."
    print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
    
def main():
    profiles_list = f1.FUNCTION_1(profiles = PROFILES, files = pro_files)
    profiles_df = profiles_list.profilesDF(profiles_list.HEADERS, profiles_list.DATA)
     
    acceptable_inputs = ["1", "2", "3", "4", "5", "6", "7"]

    # Getting student B information
    student_B_name = sys.argv[1]
    student_B_info = sb.STUDENT_B(profiles_df, student_B_name).student_B_info

    #Verifying if the user profile exist
    temp_list = []

    for name in profiles_df["Name"]:
        temp_list.append(name)
    
    if student_B_name in temp_list:
        del temp_list 

    else:
        cowsay.tux("User Profile Does Not Exist! Exiting Program!")
        exit()
        
    #Display banner & Options
    display_ui()
    options()

    # Getting user to input his/her option
    user_input = raw_input("Enter your option: ")

    # User entered a valid input
    if user_input in acceptable_inputs:

        while user_input in acceptable_inputs:
            """Put this here"""
            f2_df = f2.COUNTRY_MATCH(profiles_df, student_B_name, student_B_info).countries_matches

            # Option 1
            if user_input == "1":
                print profiles_df
                raw_input("Press Enter to continue...")
                print "\n \n"

            # Option 2
            elif user_input == "2":
                print f2_df
                raw_input("Press Enter to continue...")
                print "\n \n"

            # Option 3
            elif user_input == "3":
                f3_matches = f3.LIKES_DISLIKES(f2_df)  # calling the class LIKES_DISLIKESel
                f3_matches_lst = f3_matches.temp_list  # converting dataframe to list

                countLikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Likes")  # count the no. of likes
                countDislikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Dislikes")  # count the no. of dislikes

                f3_df = f3_matches.matches(countLikes, countDislikes, f3_matches_lst)
                print f3_df.head(n=5)[["Name", "Gender", "Rank"]]
                raw_input("Press Enter to continue...")
                print "\n \n"

            # Option 4
            elif user_input == "4":
                print "test4"
                raw_input("Press Enter to continue...")

            # Option 5
            elif user_input == "5":
                print "test5"
                raw_input("Press Enter to continue...")

            # Option 6
            elif user_input == "6":
                print "test6"
                raw_input("Press Enter to continue...")

            # Option 7
            elif user_input == "7":
                print "Thank You for Using 1002_Tinder!"
                print "Have a nice day!"
                raw_input()
                break

            options()
            user_input = raw_input("Enter your option: ")

    #User entered an invalid input 
    else:
        print "Invalid Option Entered!" 
        user_input = raw_input("Enter your option: ")
        #print "Invalid Option Entered! Exiting Program."
        #print "Thank You for Using 1002_Tinder!"


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start_time = time.time()
    main()
    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))






