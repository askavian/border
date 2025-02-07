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
        self.lod = None # Difficulty Level
        self.time = 0 # changes with difficulty level hard = 30 min / medium = 45 min / easy = 60 min
        self.score = 0 # Score between 0 and 100
        self.people = 0 # people left in the queue
        self.currentcase = "c01"
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



#### SETUP ####

def setup_game():
    os.system("cls") # cls for windows "clear" for mac

    ### NAME ###
    setup_01 = "What is your name rookie?\n" # not print because everything will come naturally
    for character in setup_01:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.05) # gives delay to input of 5 miliseconds
    player_name = input("> ") # could directly write to myPlayer.name, but keep it seperated to eventually add functionality later
    myPlayer.name = player_name

    ### DIFFICULTY LEVEL LOD ###
    setup_02 = "Select your difficulty level!\n" # not print because everything will come naturally
    setup_02_added = "(You can play on 'hard', 'medium' or 'easy')\n"
    for character in setup_02:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.05) # gives delay to input of 5 miliseconds
    for character in setup_02_added:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.01) # gives delay to input of 1 miliseconds
    player_lod = input("> ") # I could directly write to "myPlayer.lod" but keep it seperated to eventually add functionality later
    valid_lod = ["hard", "medium", "easy"]
    if player_lod.lower() in valid_lod:
        myPlayer.lod = player_lod
        print("You have " + myPlayer.time + " minutes remaining until the end of your shift!\n")
    while player_lod.lower() not in valid_lod:
        player_lod = input("> ")
        if player_lod.lower() in valid_lod:
            myPlayer.lod = player_lod
            print("You have " + myPlayer.time + " minutes remaining until the end of your shift!\n")


    #### PLAYER STATS ####
    if myPlayer.lod == "hard": # USE FOR TIME REMAINING
        myPlayer.time = 30
    elif myPlayer.lod == "medium":
        myPlayer.time = 45
    elif myPlayer.lod == "easy":
        myPlayer.time = 60




#### TESTPRINTS #### remove later
print(myPlayer.time)
print(myPlayer.name)
print(myPlayer.lod)
print(myPlayer.time)
print(myPlayer.score)
print(myPlayer.people) # change people to cases_open
print(myPlayer.currentcase)
print(myPlayer.game_over)
















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
