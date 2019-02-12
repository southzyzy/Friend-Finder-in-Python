from pyfiglet import Figlet
import cowsay
import sys
import warnings, time, os
import function1 as f1
import function2 as f2
import function3 as f3
import student_B as sb
import main

CURENT_DIR = os.path.dirname(__file__)  # specify current directory
PROFILES = os.path.join(CURENT_DIR, "profile/")  # locate the data profile
API_KEY_DIR = os.path.join(CURENT_DIR, "keys/")
pro_files = [file for file in os.listdir(PROFILES) if
             file.endswith(".txt")]  # list out all the profiles in profiles folder
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
    print "7. Exit."
    print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="


# Main Program
def ui():
    profiles_df = main.function1()

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
            if choice < 0 or choice == 0 or choice > 8:
                print ERRMSG.get(1)
                continue

        # Option 1: List all the names, gender and age from all the profiles.
        if choice == 1:
            # Display the names, gender and age from all the profiles.
            print profiles_df
            raw_input("Press Enter to return to main menu...")
            continue

        # Option 7: Exit.
        elif choice == 7:
            print "Thank You for Using 1002_Tinder!"
            print "Have a nice day!"
            program_exit = True


        # Option 2 to Option 6
        else:
            while True:
                try:
                    # Prompt the user to enter his/her profile name
                    student_B_name = raw_input("Enter a profile name => ")

                    """ This part get student B info """
                    sb_df = main.student_B(profiles_df, student_B_name)
                    print sb_df
                    if sb_df == "Error":
                        display_ui_2()

                        while True:
                            try:
                                # Prompt the user to enter an input
                                sb_choice = int(raw_input("=> "))
                            except ValueError:
                                print ERRMSG.get(1)
                                continue
                            else:
                                if sb_choice == 0 or sb_choice > 3:
                                    print ERRMSG.get(1)
                                    continue
                                else:
                                    if sb_choice == 1:
                                        print profiles_df[["Name", "Gender"]].loc[profiles_df['Gender'] == "M"]
                                    elif sb_choice == 2:
                                        print profiles_df[["Name", "Gender"]].loc[profiles_df['Gender'] == "F"]
                                    else:
                                        break
                            break

                except Exception as e:
                    break


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start_time = time.time()
    # Display banner & Options
    display_ui()
    ui()
    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))
