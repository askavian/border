# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#1##############################################################################
#2                                                                             #
#3                                                                             # 
#4                                                                             #
#5                       OUTPUT WINDOW FOR REFERENCE                           # 
#6                                                                             #
#7                                                                             #  
#8                                                                             #
#9   80 colums max-width for output window reference as set by CI template     # 
#10                                                                            #
#11                                                                            #
#12  24 rows max-height for output window as set by CI template                #
#13                                                                            #
#14                                                                            #   
#15                                                                            # 
#16                                                                            #
#17                                                                            #
#18                                                                            #
#19                                                                            #
#20                                                                            #
#21                                                                            #
#22                                                                            #
#23                                                                            #  
#24#############################################################################
# only 22 rows are used to give space for command response


# ██████   ██████  ██████  ██████  ███████ ██████            
# ██   ██ ██    ██ ██   ██ ██   ██ ██      ██   ██           
# ██████  ██    ██ ██████  ██   ██ █████   ██████            
# ██   ██ ██    ██ ██   ██ ██   ██ ██      ██   ██           
# ██████   ██████  ██   ██ ██████  ███████ ██   ██           
#                                                               
#                                                               
#  ██████ ██████   ██████  ███████ ███████ ██ ███    ██  ██████  
# ██      ██   ██ ██    ██ ██      ██      ██ ████   ██ ██       
# ██      ██████  ██    ██ ███████ ███████ ██ ██ ██  ██ ██   ███ 
# ██      ██   ██ ██    ██      ██      ██ ██ ██  ██ ██ ██    ██ 
#  ██████ ██   ██  ██████  ███████ ███████ ██ ██   ████  ██████  
#
#  by Malte M. Boettcher 

import cmd # imports command functions -> NOT USED ATM
import textwrap # displays text in wraps -> NOT USED ATM
import sys # imports system functions -> used here for "exit" command to close game
import os # imports operating systems functions -> used here for "cls" command in windows (NO "clear command used for Apple")
import time # imports time related functions -> used here for text output delay time
import random # randomizer -> used here for randomize encounters

screen_width = 100 # sets output window to full screen 100% width CHECK IF ISSUES WITH TEMPLATE RESTRICTIONS 80/24

#### PLAYER INITITAL SETUP ####
class player:
    def __init__(self):
        self.name = "" # set by player input
        self.time = 0 # changes with difficulty level hard = 30 min / medium = 45 min / easy = 60 min
        self.score = 0 # Score between 0 and 100
        self.people = 0 # people left in the queue
        self.game_over = False # primary game condition
myPlayer = player() # sets myPlayer to player class


#### TITLE SCREEN AND SETUP ####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game() # placeholder until written
    elif option.lower() == ("help"):
        help_menu() # placeholder until written
    elif option.lower() == ("quit"):
        sys.exit() # system function to exit program
    while option.lower() not in ["play", "help", "quit"]: # shows options while player is undecided
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game() # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit() # system function to exit program

def title_screen():
    os.system("cls") #clear output window
    print("                                                                                ")
    print("    Welcome to:                                                                 ")
    print("                                                                                ")
    print("    ██████   ██████  ██████  ██████  ███████ ██████                             ")
    print("    ██   ██ ██    ██ ██   ██ ██   ██ ██      ██   ██                            ")
    print("    ██████  ██    ██ ██████  ██   ██ █████   ██████                             ")  
    print("    ██   ██ ██    ██ ██   ██ ██   ██ ██      ██   ██                            ")
    print("    ██████   ██████  ██   ██ ██████  ███████ ██   ██                            ") 
    print("                                                                                ")
    print("     ██████ ██████   ██████  ███████ ███████ ██ ███    ██  ██████               ")
    print("    ██      ██   ██ ██    ██ ██      ██      ██ ████   ██ ██                    ")
    print("    ██      ██████  ██    ██ ███████ ███████ ██ ██ ██  ██ ██   ███              ")
    print("    ██      ██   ██ ██    ██      ██      ██ ██ ██  ██ ██ ██    ██              ")   
    print("     ██████ ██   ██  ██████  ███████ ███████ ██ ██   ████  ██████               ") 
    print("                                                                                ")
    print("    A game about tough moral choices and consequences.                          ")
    print("                                                                                ")
    print("    type in:                                                                    ")
    print("      - Play - Starts a new game                                                ")
    print("      - Help - Opens the help menu                                              ")
    print("      - Quit - Exits the game                                                   ")
    print("                                                                                ")
    title_screen_selections()

def help_menu():
    print("                                                                                ")
    print("    HELP MENU:                                                                  ")
    print("                                                                                ")
    print("                                                                                ")
    print("                                                                                ")
    print("                                                                                ")  
    print("                                                                                ")
    print("                                                                                ") 
    print("                                                                                ")
    print("                                                                                ")
    print("                                                                                ")
    print("                                                                                ")
    print("                                                                                ")   
    print("                                                                                ") 
    print("                                                                                ")
    print("                                                                                ")
    print("                                                                                ")
    print("    type in:                                                                    ")
    print("      - Play - Starts a new game                                                ")
    print("      - Help - Opens the help menu                                              ")
    print("      - Quit - Exits the game                                                   ")
    print("                                                                                ")
    title_screen_selections()


#### CASES OPTIONS ####

case = ""
luggage = "luggage" # to examine the belongings of an individual
search = "search" # to stripsearch an
question = "question" # to inquire about the reasons for enter 
approve = "approve" # approves the request and let the individual pass the border
deny = "deny" # deny the entry request and prevents the individual from entering 
solved = False # sets a boolean for if a case has already been closed


#### CASE DICTONARY ####
solved_cases = {"c01": False, "c02": False, "c03": False, "c04": False, "c05": False}
# dictionary can be expanded or used for shuffel
























#### TESTING SCREENS

print("#1##############################################################################")
print("#2                                                                             #")
print("#3                                                                             #") 
print("#4                                                                             #")
print("#5                       OUTPUT WINDOW FOR REFERENCE                           #")
print("#6                  Fullscreen Test with individual rows                       #")
print("#7                                                                             #")  
print("#8                                                                             #")
print("#9   80 colums max-width for output window reference as set by CI template     #") 
print("#10                                                                            #")
print("#11                                                                            #")
print("#12  24 rows max-height for output window as set by CI template                #")
print("#13                                                                            #")
print("#14                                                                            #")   
print("#15                                                                            #") 
print("#16                                                                            #")
print("#17                                                                            #")
print("#18                                                                            #")
print("#19                                                                            #")
print("#20                                                                            #")
print("#21                                                                            #")
print("#22                                                                            #")
print("#23                                                                            #")  
print("#24#############################################################################")

print("""
#1##############################################################################
#2                                                                             #
#3                                                                             # 
#4                                                                             #
#5                       OUTPUT WINDOW FOR REFERENCE                           # 
#6                 Fullscreen Test with one print command                      #
#7                                                                             #  
#8                                                                             #
#9   80 colums max-width for output window reference as set by CI template     # 
#10                                                                            #
#11                                                                            #
#12  24 rows max-height for output window as set by CI template                #
#13                                                                            #
#14                                                                            #   
#15                                                                            # 
#16                                                                            #
#17                                                                            #
#18                                                                            #
#19                                                                            #
#20                                                                            #
#21                                                                            #
#22                                                                            #
#23                                                                            #  
#24#############################################################################
      """)


print("                                                                                ")
print("    Welcome to:                                                                 ")
print("                                                                                ")
print("    ██████   ██████  ██████  ██████  ███████ ██████                             ")
print("    ██   ██ ██    ██ ██   ██ ██   ██ ██      ██   ██                            ")
print("    ██████  ██    ██ ██████  ██   ██ █████   ██████                             ")  
print("    ██   ██ ██    ██ ██   ██ ██   ██ ██      ██   ██                            ")
print("    ██████   ██████  ██   ██ ██████  ███████ ██   ██                            ") 
print("                                                                                ")
print("     ██████ ██████   ██████  ███████ ███████ ██ ███    ██  ██████               ")
print("    ██      ██   ██ ██    ██ ██      ██      ██ ████   ██ ██                    ")
print("    ██      ██████  ██    ██ ███████ ███████ ██ ██ ██  ██ ██   ███              ")
print("    ██      ██   ██ ██    ██      ██      ██ ██ ██  ██ ██ ██    ██              ")   
print("     ██████ ██   ██  ██████  ███████ ███████ ██ ██   ████  ██████               ") 
print("                                                                                ")
print("    A game about tough moral choices and consequences.                          ")
print("                                                                                ")
print("    type in:                                                                    ")
print("      - Play - Starts a new game                                                ")
print("      - Help - Opens the help menu                                              ")
print("      - Quit - Exits the game                                                   ")
print("                                                                                ")
