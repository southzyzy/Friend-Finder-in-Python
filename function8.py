'''
THe student play a game or something like guess the birthday?
Hints given when the student is guesing: give the horoscope sign, then give a math question like its in the range of(0,10) and multiple of 2. 
Let him play 3 tries. He win alr then reveal the instagram id then say Congratulations, follow him/her to start chatting with each other !!
'''

import pandas as pd
import function2 as f2
import random 

def function8(user_data):

    name_list = []

    for name in user_data["Name"]:
        name_list.append(name)

    print name_list 
        


    

    



#Maybe do like a best match 
#Then play game
#If win, reveal instagram id 


print "Congratulations, follow him/her to start chatting with each other!" 
