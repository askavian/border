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
import os # imports operating systems functions -> used here for "clear" command NOT "cls" for Heroku
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
    os.system("clear")
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
introduction = "introduction text" #personal data and passport
luggage = "luggage" # to examine the belongings of an individual
luggage_condition = 0 # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
search = "search" # to stripsearch an
search_condition = 0 # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
question = "question" # to inquire about the reasons for enter 
question_condition = 0 # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
approve = "approve" # approves the request and let the individual pass the border
approve_condition = 0 # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
deny = "deny" # deny the entry request and prevents the individual from entering 
deny_condition = 0 # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
solved = False # sets a boolean for if a case has already been closed
condition = 0 # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
good_outcome = "good outcome" # text for good outcome
good_condition = False # For storing outcome
bad_outcome = "bad outcome" # text for bad outcome
bad_condition = False # For storing outcome
secret_outcome = "secret outcome" # text for secret outcome
secret_condition = False # For storing outcome
next_case = "next" # next case in line


#### CASE DICTONARY AS KEY VALUE####
solved_cases = {"c01": False, "c02": False, "c03": False, "c04": False, "c05": False}
# dictionary can be expanded or used for shuffel

#### CASEMAP ####

casemap = {
    "c01": {
        case: "c01 name",
        introduction: "c01 intro",
        luggage: "c01 luggage",
        luggage_condition: 0,
        search: "c01 search",
        search_condition: 3,
        question: "c01 question", 
        question_condition: 0,
        approve: "c01 approve",
        approve_condition: 2,
        deny: "c01 deny",
        deny_condition: 1, 
        solved: False,
        condition: 0,
        good_outcome: "c01 good outcome",
        good_condition: False,
        bad_outcome: "c01 bad outcome",
        bad_condition: False,
        secret_outcome: "c01 secret outcome",
        secret_condition: False,
        next_case: "c02",
    },
    "c02": {
        case: "c02 name",
        introduction: "c02 intro",
        luggage: "c02 luggage",
        luggage_condition: 0,
        search: "c02 search",
        search_condition: 0,
        question: "c02 question",
        question_condition: 0, 
        approve: "c02 approve",
        approve_condition: 0,
        deny: "c02 deny", 
        deny_condition: 0,
        solved: False,
        condition: 0,
        good_outcome: "c02 good outcome",
        good_condition: False,
        bad_outcome: "c02 bad outcome",
        bad_condition: False,
        secret_outcome: "c02 secret outcome",
        secret_condition: False,
        next_case: "c03",
    },
    "c03": {
        case: "c03 name",
        introduction: "c03 intro",
        luggage: "c03 luggage",
        luggage_condition: 0,
        search: "c03 search",
        search_condition: 0,
        question: "c03 question",
        question_condition: 0, 
        approve: "c03 approve",
        approve_condition: 0,
        deny: "c03 deny", 
        deny_condition: 0,
        solved: False,
        condition: 0,
        good_outcome: "c03 good outcome",
        good_condition: False,
        bad_outcome: "c03 bad outcome",
        bad_condition: False,
        secret_outcome: "c03 secret outcome",
        secret_condition: False,
        next_case: "c04",
    },
        "c04": {
        case: "c04 name",
        introduction: "c04 intro",
        luggage: "c04 luggage",
        luggage_condition: 0,
        search: "c04 search",
        search_condition: 0,
        question: "c04 question",
        question_condition: 0, 
        approve: "c04 approve",
        approve_condition: 0,
        deny: "c04 deny", 
        deny_condition: 0,
        solved: False,
        condition: 0,
        good_outcome: "c04 good outcome",
        good_condition: False,
        bad_outcome: "c04 bad outcome",
        bad_condition: False,
        secret_outcome: "c04 secret outcome",
        secret_condition: False,      
        next_case: "c05",
    },
        "c05": {
        case: "c05 name",
        introduction: "c05 intro",
        luggage: "c05 luggage",
        luggage_condition: 0,
        search: "c05 search",
        search_condition: 0,
        question: "c05 question",
        question_condition: 0, 
        approve: "c05 approve",
        approve_condition: 0,
        deny: "c05 deny", 
        deny_condition: 0,
        solved: False,
        condition: 0,
        good_outcome: "c05 good outcome",
        good_condition: False,
        bad_outcome: "c05 bad outcome",
        bad_condition: False,
        secret_outcome: "c05 secret outcome",
        secret_condition: False,
        next_case: "",
    },
}

#### GAME INTERACTIVITY ####
def print_currentcase():
    print("\n" + ("#" * (4 + len(myPlayer.currentcase)))) # "\n" prints everything on a new line / make # x 4 len(myPlayer.currentcase) gets the LENGTH OF THE STRING of location
    print("REQUEST FOR ENTRY: ")
    print("# " + casemap
          [myPlayer.currentcase] [introduction])

def prompt():  
    print("\n" + "===================")
    print("What would you like to do?")
    print(casemap[myPlayer.currentcase] [secret_condition]) # FOR TESTING
    print(casemap[myPlayer.currentcase] [solved]) # FOR TESTING
    print(myPlayer.people)
    action = input("> ")
    acceptable_actions = ["luggage", "search", "question", "approve", "deny", "quit"]
    while action.lower() not in acceptable_actions:
        print("Unkonw action, try again.\n")
        action = input("> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() == "luggage":
        myPlayer.time = myPlayer.time - 8
        print("# " + casemap
          [myPlayer.currentcase] [luggage])
    elif action.lower() == "search":
        myPlayer.time = myPlayer.time - 10
        print("# " + casemap[myPlayer.currentcase] [search])
        while action.lower() == "search":
            if casemap[myPlayer.currentcase] [search_condition] == 3: # BUGGY
                print("This is true") # BUGGY
    elif action.lower() == "question":
        myPlayer.time = myPlayer.time - 5
        print("# " + casemap
          [myPlayer.currentcase] [question])
    elif action.lower() == "deny":
        myPlayer.time = myPlayer.time - 2
        print("# " + casemap
          [myPlayer.currentcase] [deny])
    elif action.lower() == "approve":
        myPlayer.time = myPlayer.time - 1
        print("# " + casemap
          [myPlayer.currentcase] [approve])


#### GAME FUNCTIONALITY ####
def main_game_loop():
    while myPlayer.game_over is False:
        print("You have " + str(myPlayer.time) + " minutes remaining until the end of your shift!\n")  
        print_currentcase()
        prompt()
        if myPlayer.time < 0: # FAILING CONDITION "run out of time"
            myPlayer.game_over
            print("You ran out of time! You lost the game!")
            sys.exit()


#### SETUP ####

def setup_game():
    os.system("clear")

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
    while player_lod.lower() not in valid_lod:
        player_lod = input("> ")
        if player_lod.lower() in valid_lod:
            myPlayer.lod = player_lod


    #### PLAYER STATS ####
    if myPlayer.lod == "hard": # USE FOR TIME REMAINING
        myPlayer.time = 30
        myPlayer.people = 5 # Equal to the number of cases
    elif myPlayer.lod == "medium":
        myPlayer.time = 45
        myPlayer.people = 5
    elif myPlayer.lod == "easy":
        myPlayer.time = 60
        myPlayer.people = 5
    
    print("You have " + str(myPlayer.time) + " minutes remaining until the end of your shift!\n")


    #### STARTS GAME AFTER SETUP ####
    os.system("clear") 
    print("########################")
    print("#   Let's Start now!   #")
    print("########################")
    main_game_loop()

title_screen() # launches the game and setup









#### TESTPRINTS #### remove later
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



# DO NOT USE looks wierd 
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
