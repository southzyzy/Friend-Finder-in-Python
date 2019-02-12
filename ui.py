from pyfiglet import Figlet
import cowsay
import sys
import random
import warnings, time, os
import function1 as f1
import function2 as f2
import function3 as f3
import function7 as f7
import student_B as sb

#Specify current directory
CURENT_DIR = os.path.dirname(__file__)  

#Locate the data profile
PROFILES = os.path.join(CURENT_DIR, "profile/")  

API_KEY = os.path.join(CURENT_DIR, "keys/")

#List out all the profiles in profiles folder
pro_files = [file for file in os.listdir(PROFILES) if
             file.endswith(".txt")]  

#List out the api-keys in keys folder
key_files = [file for file in os.listdir(API_KEY) if file.endswith(".bin")]  

#Function to display the main menu 
def display_ui():
    ui_banner = Figlet(font = "graffiti")
    print ui_banner.renderText("Welcome To 1002_Tinder")
    cowsay.cow("Wanna Get Hitch? Use 1002_Tinder!")
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
    print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="

#Main Program 
def main():
    profiles_list = f1.FUNCTION_1(profiles = PROFILES, files = pro_files)

    #Store all the data in the profiles into Data Frames 
    profiles_df = profiles_list.profilesDF(profiles_list.HEADERS, profiles_list.DATA)

    #Display banner & Options
    display_ui()

    #Prompt the user to input his/her option
    user_input = raw_input("Enter your option: ")

    #Variable to determine the state of the program 
    program_exit = False
    
    while program_exit != True:
        
        #Option 1: List all the names, gender and age from all the profiles.
        if user_input == "1":

            #Display the names, gender and age from all the profiles.
            print profiles_df
            raw_input("Press Enter to continue...")
            os.system("cls")
            display_ui()
            
            #Prompt the user to input his/her option
            user_input = raw_input("Enter your option: ")

        #Option 8: Exit.
        elif user_input == "8":
            print "Thank You for Using 1002_Tinder!"
            print "Have a nice day!"
            program_exit = True
            
        #Option 2 to Option 6 
        elif user_input == "2" or user_input == "3" or user_input == "4" or user_input == "5" or user_input == "6" or user_input == "7":
            
            #Promt the user to enter his/her profile name 
            student_B_name = raw_input("Enter a profile name: ")

            #Verifying that the user profile exist within the application 
            temp_list = []

            for name in profiles_df["Name"]: 
                temp_list.append(name)

            #Scenario 1: User Profile exists 
            if student_B_name in temp_list: 
                del temp_list

                #Store Student B's information into a variable 
                student_B_info = sb.STUDENT_B(profiles_df)
                student_B_info = student_B_info.check_name(student_B_name)

                f2_df = f2.COUNTRY_MATCH(profiles_df, student_B_name, student_B_info).countries_matches

                #Option 2: List all the matched students of one given student B based on country.
                if user_input == "2":
                    print f2_df
                    raw_input("Press Enter to continue...")
                    os.system("cls")
                    display_ui()

                    #Prompt the user to input his/her option
                    user_input = raw_input("Enter your option: ")


                #Option 3: List the top 3 best matched students who share the most similar likes or dislikes for one given student B.
                elif user_input == "3":
                    
                    #Calling the class LIKES_DISLIKES
                    f3_matches = f3.LIKES_DISLIKES(f2_df)

                    #Converting dataframe to list
                    f3_matches_lst = f3_matches.temp_list
                    
                    #Count the no. of likes
                    countLikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Likes")

                    #Count the no. of dislikes
                    countDislikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Dislikes")  

                    #Store the data of the matched profiles into a data frame 
                    f3_df = f3_matches.matches(countLikes, countDislikes, f3_matches_lst)
                    
                    print f3_df.head(n=5)[["Name", "Gender", "Rank"]]
                    raw_input("Press Enter to continue...")
                    os.system("cls")
                    display_ui()

                    #Prompt the user to input his/her option
                    user_input = raw_input("Enter your option: ")

                #Option 4: List the top 3 best matched students based on books they like.
                elif user_input == "4":
                    print "test4"
                    raw_input("Press Enter to continue...")
                    os.system("cls")
                    display_ui()

                    #Prompt the user to input his/her option
                    user_input = raw_input("Enter your option: ")

                #Option 5: List the top 3 best matched students based on the overall profile information which may include all the personal information for ranking.
                elif user_input == "5":
                    print "test5"
                    raw_input("Press Enter to continue...")
                    os.system("cls")
                    display_ui()

                    #Prompt the user to input his/her option
                    user_input = raw_input("Enter your option: ")

                #Option 6: Store all the best matched students into one .csv file on the disk.
                elif user_input == "6":
                    print "\n"
                    
                    #Prompt the user to enter the file name of the .csv file 
                    file_name = raw_input("Enter a file name: ")

                    #calling the class LIKES_DISLIKESel
                    f3_matches = f3.LIKES_DISLIKES(f2_df)  

                    #converting dataframe to list
                    f3_matches_lst = f3_matches.temp_list  

                    #count the no. of likes
                    countLikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Likes")

                    #count the no. of dislikes
                    countDislikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Dislikes")  

                    f3_df = f3_matches.matches(countLikes, countDislikes, f3_matches_lst)

                    #Export to csv file 
                    f3_df.to_csv(file_name + ".csv")
                    
                    print "File Successfully exported!"
                                    
                    raw_input("Press Enter to continue...")
                    os.system("cls")
                    display_ui()

                    #Prompt the user to input his/her option
                    user_input = raw_input("Enter your option: ")


                # Option 7: Play birthday guessing game
                elif user_input == "7":
                    print "\n"
                    # Calling the class LIKES_DISLIKES
                    f3_matches = f3.LIKES_DISLIKES(f2_df)

                    # Converting dataframe to list
                    f3_matches_lst = f3_matches.temp_list

                    # Count the no. of likes
                    countLikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Likes")

                    # Count the no. of dislikes
                    countDislikes = f3_matches.countMatch(f3_matches_lst, student_B_info, "Dislikes")

                    # Store the data of the matched profiles into a data frame
                    f3_df = f3_matches.matches(countLikes, countDislikes, f3_matches_lst)

                    # Initialize function 7 and get a list of matched profiles
                    game = f7.openFunction(f3_df)
                    exclude_profile = []  # This is for excluding profiles that have done the game
                    count = 0
                    while count < len(game.profiles):
                        # Randomly select a profile that has not been used for the game
                        random_profile = random.sample([i for i in game.profiles if i not in exclude_profile], 1)
                        # Add the selected profile into the exclude list
                        exclude_profile.append(random_profile[0])
                        count += 1
                        print game.getGameIntro(random_profile)  # Print intro + hints
                        choices = game.choiceGenerator()
                        correctAnswer = game.getAnswer(choices)
                        print game.tupleListDecoder(choices)  # Print multiple choices
                        attempts = 3
                        while attempts > 0:
                            user_input = raw_input("What is their birthday?(Select by number, i.e 1!): ")
                            gameData = game.startGame(user_input, attempts,
                                                      correctAnswer)  # Printstring[0], attempt number[1]
                            print gameData[0]
                            attempts = gameData[1]
                        while True:
                            # Ask player if they wish to guess another candidate. Limit to the number of available candidates (5 people likely)
                            answer = raw_input(
                                "Would you like to guess another one of your top few most matched candidate(Y/N)?:")
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

                    raw_input("Press Enter to continue...")
                    os.system("cls")
                    display_ui()

                    # Prompt the user to input his/her option
                    user_input = raw_input("Enter your option: ")

            #Scenario 2: User Profile Does Not Exist 
            else:
                #Display the second menu 
                def display_ui_2():
                    os.system("cls")
                    cowsay.tux("User Profile Does Not Exist Within Our Database!")
                    print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
                    print "Do You Wish To Display the Names of Students of a Specific Gender?"
                    print "1. Display the Names of All Male Students."
                    print "2. Display the Names of All Female Students."
                    print "3. Return to Main Menu."
                    print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
                
                #Display the second menu 
                display_ui_2()

                #Prompt the user to enter an input 
                user_input_2 = raw_input("Enter your option: ")

                #Variable to determine the state of the program 
                program_exit_2 = False
                
                while program_exit_2 != True:
                    
                    #Option 1: Display the names of all the male students 
                    if user_input_2 == "1":

                        #Display the names of all the male students 
                        print profiles_df[profiles_df['Gender'] == "M"]

                        raw_input("Press Enter to continue...")
                        os.system("cls")
                        display_ui_2()
                        user_input_2 = raw_input("Enter your option: ")
                     
                    #Option 2: Display the names of all the female students 
                    elif user_input_2 == "2":

                        #Display the names of all the female students 
                        print profiles_df[profiles_df['Gender'] == "F"]

                        raw_input("Press Enter to continue...")
                        os.system("cls")
                        display_ui_2()
                        user_input_2 = raw_input("Enter your option: ")
                    
                    #Option 3: Return to Main Menu  
                    else:
                        os.system("cls")
                        program_exit_2 = True
                        display_ui()
                        user_input = raw_input("Enter your option: ")
                        
        #User Entered an Invalid Input 
        else:
            print "Invalid Input Entered! \n" 
            user_input = raw_input("Please Re-Enter your option: ")
			
if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    start_time = time.time()
    main()
    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))
