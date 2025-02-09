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


import sys # imports system functions -> used here for "exit" command to close game
import os # imports operating systems functions -> used here for "clear" command NOT "cls" for Heroku
import time # imports time related functions -> used here for text output delay time

screen_width = 100 # sets output window to full screen 100% width


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
    print("                                                                                ")
    print("    type in:                                                                    ")
    print("      - Play - Starts a new game                                                ")
    print("      - Help - Opens the help menu                                              ")
    print("      - Quit - Exits the game                                                   ")
    title_screen_selections()

def help_menu():
    print("                                                                                ")
    print("    HELP MENU:                                                                  ")
    print("                                                                                ")
    print("    It is your first day as a new Officer of the Border Force and it is your    ")
    print("    job to decide if someone can enter the country or not.                      ")
    print("    You can perform the following actions by typing in the respective command:  ")
    print("                                                                                ") 
    print("    COMMAND     ACTION                                               TIME NEEDED")
    print("    =======     ======                                               ===========")
    print("  - Luggage -   Search the belongings of an individual.               8 minutes ")
    print("  - Search -    Perform a strip search of an individual.             12 minutes ")
    print("  - Question -  Question the individual on the reason for entry.      5 minutes ")   
    print("  - Approve -   Entry is granted and the individual can enter.        1 minute  ") 
    print("  - Deny -      Entry is rejected and the individual is send back.    2 minutes ")
    print("                                                                                ")
    print("    Depending on the Level of Difficulty chosen, you only a set amount of time  ")
    print("    until your shift end: 30 min (HARD), 45 min (MEDIUM) or 60 min (EASY)       ")
    print("                                                                                ")
    print("    type in:                                                                    ")
    print("      - Play - Starts a new game                                                ")
    print("      - Help - Opens the help menu                                              ")
    print("      - Quit - Exits the game                                                   ")
    title_screen_selections()


#### CASES OPTIONS ####

case = "CASE"
introduction = "INTRO" #personal data and passport
luggage = "LUGGAGE" # to examine the belongings of an individual
luggagecondition = "LUGGCOND" # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
search = "SEARCH" # to stripsearch an
searchcondition = "SEARCOND" # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
question = "QUESTION" # to inquire about the reasons for enter 
questioncondition = "QUESCOND" # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
approve = "APPROVE" # approves the request and let the individual pass the border
approvecondition = "APPRCOND" # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
deny = "DENY" # deny the entry request and prevents the individual from entering 
denycondition = "DENYCOND" # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
solved = "SOLVED" # sets a boolean for if a case has already been closed
condition = "CONDITION" # 1 (good outcome), 2 (bad outcome), 3 (secret outcome if available)
goodoutcome = "GOODOUT" # text for good outcome
goodcondition = "GOODCOND" # For storing outcome
badoutcome = "BADOUT" # text for bad outcome
badcondition = "BADCOND" # For storing outcome boolean
secretoutcome = "SECOUT" # text for secret outcome
secretcondition = "SECCOND" # For storing outcome
nextcase = "NEXT" # next case in line


#### CASEMAP ####

casemap = {
    "c01": {
    case: "Lanto Blorg",

    introduction: """
    Name: Lanto Blorg
    Date of Birth: Dec.11th, 1999
    Sex: Male

    The passport was recently issued and shows no obvious signs of damage or 
    manipulation.
    You recognize the person in front of you as the same person shown on the
    passport photo. 
    The eyes are the same; the shape of the ears is the same and you 
    recognize a birthmark beneath the left eye.

    However, in his passport, the person has a full beard and hair. The man 
    in front of you is bald and fully shaven.      
    """,
    luggage: """
    You go through Lanto's luggage and find:
    
    # A few personal belongings. Among them a picture of his family and a 
      religious object. 
    # Clothing items that are in remarkable condition (brand new). But the
      amount of clothing seems off. There is only one pair of underwear, 
      but five shirts and two pair of suit pants. 
    # No fluids, alcohol or any other contraband. 

    There is no contraband in Lanto's suitcase or any other illegal items.
    """,
    luggagecondition: 0,
    search: """
    You perform a full check on Lanto and his belonging. 
                  
    You find 2kg of C4 inside a suicide vest underneath his shirt and a 
    detailed list of a planned attack in the city.
               
    Lanto is arrested!
    """,
    searchcondition: 3,
    question: """
    At first, Lanto is hestitant to answer your questions, but after a while
    he opens up. 
    Lanto plans on staying at least two weeks in the city. 
   
    His plans are to search for his family that got seperated during the 
    war. Unfortunately, he has no place to stay and no Hotel Reservation. 
    This is odd, because usually, people are booking their accomodation way
    in advance within a secure Hotel with Security when visiting.
    """, 
    questioncondition: 0,
    approve: """
    Lanto Blorg passes through the border crossing uninterrupted.
    """,
    approvecondition: 2,
    deny: """
    Lanto Blorg is shouting about racial profiling and why you refuse him. 
    But ultimately he leaves the border crossing and returns home.
    """,
    denycondition: 1, 
    solved: False,
    condition: 0,
    goodoutcome: """
    A would-be suicide attacker was rejected today at the border crossing. 
    The man was later identified as Lanto Blorg.
    He tried to cross the border but was rejected. On his way back home his
    sucide vest went off killing only him.
    """,
    goodcondition: False,
    badoutcome: """
    A Terrorist Attack happend on a public bus this afternoon, killing 15 
    and injuring 7, including children. 
    The individual was later identified as Lanto Blorg and was able to pass
    the border uniterrupted while carrying a suicide vest. 
    """,
    badcondition: False,
    secretoutcome: """
    A Terrorist Attack was prevented today thanks to a new border guard 
    officer on his first day of duty!
    While searching the would-be terrorist, identified as Lanto Blorg, the 
    guard noticed a suicide vest. 
    The guard took immediate action and in such prevented a disaster.
    """,
    secretcondition: False,
    nextcase: "c02",
    },
    "c02": {
    case: "Dammyra de Brillaal",
    introduction: """
    Name: Dammyra de Brillaal
    Date of Birth: June.5th, 2004
    Sex: Female

    The passport is unremarkable and the details check out. Dammyra is the 
    individual in the pictures.
    She wears full make-up (maybe a bit too much) and from the optics, she
    can be considered beautiful.  

    Her behavior seems to erratic, however, and while talking to you, she
    constantly looks over her shoulder. 

    Maybe she is fleeing something.... or someone.      
    """,
    luggage: """
    Dammyra's luggage is hastely thrown together. Crucial items are missing. 

    There is not toothbrush and very few personal items besides clothing. 
     
    You find a worn-out Teddybear and a picture of Dammyra in a much younger
    age with an older woman. Both woman look happy. 
        
    You find a small amount of Marihuana in a alittle plastic bag at the 
    bottom of the suitcase. 
        
    The amount is small, but it is still illegal. 
    """,
    luggagecondition: 0,
    search: """
    You search Dammyra. She is visibly uncomfortable.  

    There is no forbidden item on her body, but her body shows signs of 
    violence. 

    The heavy make-up she is wearing covers up a bruise beneath her left 
    eye and on her chest, there are multiple bruises. 

    The injuries are not fresh. Maybe 4 days to a 2 weeks old and in 
    different stages of healing. 

    You also find a name tatooed on her left thigh and her arms show heavy 
    signs of substance abuse.

    This might be a mark of a pimp. 
    """,
    searchcondition: 0,
    question: """
    Dammyra claims to be visiting her sister.  

    While questioning Dammyra becomes nervous and gives answers that don't 
    add up.  
    The adress she provides does not exist and she changes the name of her 
    sister during the interview. 

    After being called on it, she breaks and begings to cry and sob 
    uncotrolably. 

    She now claims to be going back home after being obducted 5 years ago 
    by a group of human-traffickers.

    She was able to flee this morning.

    She might be lying but in the end her story checks out and you hand her 
    over to the authorities.   
    """,
    questioncondition: 3, 
    approve: """
    When you stamp her passport, you can see the relief on Dammyra's face. 
    She passes the border uniterrupted. 
    """,
    approvecondition: 1,
    deny: """
    Dammyra is visibly upset and frightend. She hestitates to walk back, but
    in the en, she gives up and leaves. 
    """, 
    denycondition: 2,
    solved: False,
    condition: 0,
    goodoutcome: """
   
    A group of criminals roaming a neighborhood tonight was arrested by the 
    police.
    When questioned the police found evidence that the group was looking for
    young woman that was reported missing 5 years ago.
    The woman did not show up at home one night and was presumed dead. 
    """,
    goodcondition: False,
    badoutcome: """
    A woman later idetified as Dammyra de Brillaal was refused entry at the 
    border today and was later found dead.
    Dammyra went missing from her parents house five years ago and was 
    presumed dead. 
    Her body was found in a dumpster and showed obvious signs of violence. 
    Our neighbours police force is leading the investigation. 
    """, 
    badcondition: False,
    secretoutcome: """
    A woman missing for five years was reunited with her mother today. She
    was spüotted entering the country at the border and after showing signs 
    of abuse was handed over to protection agencies. 
    The police said that the information gathered by her could lead to a 
    breakthrough in a human-trafficking case in both countries. 
    """,
    secretcondition: False,
    nextcase: "c03",
    },
    "c03": {
    case: "Solomon Candlegorn",
    introduction: """
    Name: Solomon Candlegorn
    Date of Birth: August.25th, 1965
    Sex: Male

    The passport is old and has only a few days until it's expiration date.
    Usually, passports must be valid at least 30 days at the point of entry.

    Tha passport marks Solomon as a member of medical aid group.

    The Picture is quite dated. He has full hair and a beard, but you can 
    see that the individual presenting to you is the same. But 10-15 years
    older.      
    """,
    luggage: """
    During the search through Solomons luggage you find clothing, personal
    hygene products, a notebook and a few books on medicine. 

    You also find a letter from the WHO recommending Solomon for work on a 
    viral outbreak in the country after the war. 

    You approve Solomon's Entry request regardles of his passport validity
    and give the Ministry of Health a call. 

    The MoH is already expecting him and are sending a vahicle to pick him 
    up right away.   
    """,
    luggagecondition: 3,
    search: """
    Solomon is embaressed by the search procedure. 

    You find nothing of value. 
    
    Just a naked old man. 
    """,
    searchcondition: 0,
    question: """
    Solomon seems bothered by your questions and a bit annoyed. 

    After a while he claims to work for the World Health Organisation and he
    claims to be an expert viologist. 

    He want's to help after the war.   
    """,
    questioncondition: 0, 
    approve: """ 
    You approve Solomons entry request and he slowly walks to the taxis
    waiting outside.   
    """,
    approvecondition: 1,
    deny: """
    You deny Solomons request for entry. He seems irritated by that, but 
    after a short while he says: 'Fine. I go on vacation. I don't like 
    being here anyway.' and walks away.  
    """,
    denycondition: 2,
    solved: False,
    condition: 0,
    goodoutcome: """
    The famous WHO Virologist: Dr. Solomon Candlegorn arrived today in our
    glorious nation to help with a viulent outbreak in the most devestated 
    parts of the country. Unfortunately, Dr. Candelgorn stuck in traffic 
    so he wasn't able to begin work right away. This may lead to some more 
    people getting infected. 
    """,
    goodcondition: False,
    badoutcome: """ 
    The famous WHO Virologist: Dr. Solomon Candlegorn was sheduled to arrive
    today in our glorious nation, but was held up and refused entry by a new
    guard at the border. It is unclear when he will be able to visit again,
    because he is currently missing. This might lead to a significant 
    outbreak or even a pandemic. 
    """,
    badcondition: False,
    secretoutcome: """  
    The famous WHO Virologist: Dr. Solomon Candlegorn arrived today in our
    glorious nation to help with a viulent outbreak in the most devestated 
    parts of the country. A Rookie Border Guard spotted the famous scientist
    and fasttracked his entry so he was able to avoid traffic and got to 
    work right away. 
    """,
    secretcondition: False,
    nextcase: "c04",
    },
    "c04": {
    case: "Adettel Hovelweir",
    introduction: """
    Name: Adettel Hovelweir
    Date of Birth: September.11th, 1987
    Sex: Female

    The passport shows no obvious signs of forgery and the picture shows 
    the woman presenting to you. 

    You recognize Adettel from somewhere. Maybe and old school acquaintance
    or someone on TV. You cannot tell.      
    """,
    luggage: """
    Name: Adettel Hovelweir
    Date of Birth: September.11th, 1987
    Sex: Female

    The passport shows no obvious signs of forgery and the picture shows 
    the woman presenting to you. 

    You recognize Adettel from somewhere. Maybe and old school acquaintance
    or someone on TV. You cannot tell.      
    """,
    luggagecondition: 0,
    search: """
    #24#####################################################################  
    Name: Adettel Hovelweir
    Date of Birth: September.11th, 1987
    Sex: Female

    The passport shows no obvious signs of forgery and the picture shows 
    the woman presenting to you. But the passport shows signs of damage and
    some stains that look like blood. 

    Adettel looks roughed up. A woman who is obviously fond of hard labour 
    and doesn't use make-up very often. She wears a bandana and work-out 
    old military clothing. 

    You recognize Adettel from somewhere. Maybe and old school acquaintance
    or someone on TV. 
    
    You cannot tell.      
    """,
    searchcondition: 0,
    question: """
    #24#####################################################################  
    Name: Adettel Hovelweir
    Date of Birth: September.11th, 1987
    Sex: Female

    The passport shows no obvious signs of forgery and the picture shows 
    the woman presenting to you. But the passport shows signs of damage and
    some stains that look like blood. 

    Adettel looks roughed up. A woman who is obviously fond of hard labour 
    and doesn't use make-up very often. She wears a bandana and work-out 
    old military clothing. 

    You recognize Adettel from somewhere. Maybe and old school acquaintance
    or someone on TV. 
    
    You cannot tell.      
    """,
    questioncondition: 0, 
    approve: "c04 approve",
    approvecondition: 1,
    deny: "c04 deny", 
    denycondition: 2,
    solved: False,
    condition: 0,
    goodoutcome: "c04 good outcome",
        goodcondition: False,
        badoutcome: "c04 bad outcome",
        badcondition: False,
        secretoutcome: "c04 secret outcome",
        secretcondition: False,      
        nextcase: "c05",
    },
        "c05": {
        case: "c05 name",
        introduction: "c05 intro",
        luggage: "c05 luggage",
        luggagecondition: 0,
        search: "c05 search",
        searchcondition: 0,
        question: "c05 question",
        questioncondition: 0, 
        approve: "c05 approve",
        approvecondition: 1,
        deny: "c05 deny", 
        denycondition: 2,
        solved: False,
        condition: 0,
        goodoutcome: "c05 good outcome",
        goodcondition: False,
        badoutcome: "c05 bad outcome",
        badcondition: False,
        secretoutcome: "c05 secret outcome",
        secretcondition: False,
        nextcase: "",
    },
}
#### GAME INTERACTIVITY ####
def print_currentcase():
    print("\n" + ("#" * (4 + len(myPlayer.currentcase))))
    print("REQUEST FOR ENTRY: ")
    speech = casemap[myPlayer.currentcase] [introduction]
    for character in speech:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.001)

def prompt():  
    print("\n" + "===================")
    print("'search' the luggage, 'question' the individual, 'search' the individual, 'deny' or 'approve' the entry")
    print("What would you like to do?\n")
    action = input("> ")
    acceptable_actions = ["luggage", "search", "question", "approve", "deny", "quit"]
    while action.lower() not in acceptable_actions:
        print("That is not a valid Action\n")
        action = input("> ")
    if action.lower() == "quit":
        print("Goodbye! Reload the Game to try again.")
        sys.exit()
    elif action.lower() == "luggage":
        player_luggage(action.lower())
    elif action.lower() == "search":
        player_search(action.lower())
    elif action.lower() == "question":
        player_question(action.lower())
    elif action.lower() == "deny":
        player_deny(action.lower())
    elif action.lower() == "approve":
        player_approve(action.lower())

def player_luggage(action):
    myPlayer.time = myPlayer.time - 8
    speech = casemap[myPlayer.currentcase] [luggage]
    for character in speech:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.05)
    if casemap[myPlayer.currentcase] [luggagecondition] == 3:
        casemap[myPlayer.currentcase] [condition] = 3
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [secretcondition] = True
        player_nextcase()

def player_search(action):
    myPlayer.time = myPlayer.time - 12
    speech = casemap[myPlayer.currentcase] [search]
    for character in speech:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.05)
    if casemap[myPlayer.currentcase] [searchcondition] == 3:
        casemap[myPlayer.currentcase] [condition] = 3
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [secretcondition] = True
        player_nextcase()

def player_question(action):
    myPlayer.time = myPlayer.time - 5
    speech = casemap[myPlayer.currentcase] [question]
    for character in speech:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.05)
    if casemap[myPlayer.currentcase] [questioncondition] == 3:
        casemap[myPlayer.currentcase] [condition] = 3
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [secretcondition] = True
        player_nextcase()

def player_approve(action):
    myPlayer.time = myPlayer.time - 1
    speech = casemap[myPlayer.currentcase] [approve]
    for character in speech:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.05)
    if casemap[myPlayer.currentcase] [approvecondition] == 1:
        casemap[myPlayer.currentcase] [condition] = 1
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [goodcondition] = True
        player_nextcase()
    elif casemap[myPlayer.currentcase] [approvecondition] == 2:
        casemap[myPlayer.currentcase] [condition] = 2
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [badcondition] = True
        player_nextcase()

def player_deny(action):
    myPlayer.time = myPlayer.time - 2
    speech = casemap[myPlayer.currentcase] [deny]
    for character in speech:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.05)
    if casemap[myPlayer.currentcase] [denycondition] == 1:
        casemap[myPlayer.currentcase] [condition] = 1
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [goodcondition] = True
        player_nextcase
    elif casemap[myPlayer.currentcase] [denycondition] == 2:
        casemap[myPlayer.currentcase] [condition] = 2
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [badcondition] = True
        player_nextcase()


def player_nextcase():
    os.system("clear")
    myPlayer.people = myPlayer.people - 1
    if myPlayer.people == 0:
        endspeech = "Your shift ended Rookie.\n" 
        endspeech = "You can go home now. Get some rest.\n"
        for character in endspeech:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        final()
    else:
        myPlayer.currentcase = casemap[myPlayer.currentcase] [nextcase]


#### FINAL ASSESSMENT ####
def final():
   time.sleep(2.5)
   newsspeech = "Welcome to today's Evening News!\n" # not print because everything will come naturally
   for character in newsspeech:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.05)
   print(""
                  
         "") 
   if casemap["c01"] [condition] == 3:
       myPlayer.score = myPlayer.score + 20
       print(casemap["c01"] [secretoutcome] + "\n")
   elif casemap["c01"] [condition] == 1:
       myPlayer.score = myPlayer.score + 10
       print(casemap["c01"] [goodoutcome] + "\n")
   elif casemap["c01"] [condition] == 2:
       myPlayer.score = myPlayer.score + 1        
       print(casemap["c01"] [badoutcome] + "\n")
   if casemap["c02"] [condition] == 3:
       myPlayer.score = myPlayer.score + 20
       print(casemap["c02"] [secretoutcome] + "\n")
   elif casemap["c02"] [condition] == 1:
       myPlayer.score = myPlayer.score + 10
       print(casemap["c02"] [goodoutcome] + "\n")
   elif casemap["c02"] [condition] == 2:
       myPlayer.score = myPlayer.score + 1   
       print(casemap["c02"] [badoutcome] + "\n")
   if casemap["c03"] [condition] == 3:
       myPlayer.score = myPlayer.score + 20
       print(casemap["c03"] [secretoutcome] + "\n")
   elif casemap["c03"] [condition] == 1:
       myPlayer.score = myPlayer.score + 10
       print(casemap["c03"] [goodoutcome] + "\n")
   elif casemap["c03"] [condition] == 2:
       myPlayer.score = myPlayer.score + 1   
       print(casemap["c03"] [badoutcome] + "\n")
   if casemap["c04"] [condition] == 3:
       myPlayer.score = myPlayer.score + 20
       print(casemap["c04"] [secretoutcome] + "\n")
   elif casemap["c04"] [condition] == 1:
       myPlayer.score = myPlayer.score + 10
       print(casemap["c04"] [goodoutcome] + "\n")
   elif casemap["c04"] [condition] == 2:
       myPlayer.score = myPlayer.score + 1   
       print(casemap["c04"] [badoutcome] + "\n")
   if casemap["c05"] [condition] == 3:
       myPlayer.score = myPlayer.score + 20
       print(casemap["c05"] [secretoutcome] + "\n")
   elif casemap["c05"] [condition] == 1:
       myPlayer.score = myPlayer.score + 10
       print(casemap["c05"] [goodoutcome] + "\n")
   elif casemap["c05"] [condition] == 2:
       myPlayer.score = myPlayer.score + 1   
       print(casemap["c05"] [badoutcome] + "\n")
   print(""
              
         "")
   newsspeech = """
   What a wild day that was, right? Goodnight and stay safe.\n
   """
   print("You scored " + str(myPlayer.score) + " out of 100.")
   for character in newsspeech:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.05)  

 
   time.sleep(60) # prevents the game from closing for 60 seconds, to read the outcome
   myPlayer.game_over = True


#### GAME FUNCTIONALITY ####
def main_game_loop():
    while myPlayer.game_over is False:
        print("""
              
              You have """ + str(myPlayer.time) + """ minutes remaining until the end of your shift!\n
              
              """)  
        print_currentcase()
        prompt()
        if myPlayer.time < 0: # FAILING CONDITION "run out of time"
            myPlayer.game_over
            print("""
                  You shift ended and there are still people waiting.
                  
                  You Lost!""")
            sys.exit()


#### SETUP ####

def setup_game():
    os.system("clear")

    ### NAME ###
    setup_01 = """
    Welcome to the border rookie!              
 
    We have fought a long and bloody war againt our neighbors and a lot of 
    good people died!

    But thanks to the might of our army and our glorious overlords we have 
    won!

    The situation on the border now is stable, but don't be fooled! Even the 
    tiniest spark can reignite hostilities.
    There are religious zealots, political extremists and criminals trying
    to seize the opportunity. Contraband Items, Weapons, Human-Traffiking, we 
    got it all!
    There are also a lot of great folks out here. Folks that we need to let 
    it. Aid-Workers, Refugees, displaced people and folks that are looking for
    a way home. 

    If we want to have a bright future with our neighbors, we have to make 
    this work!. 

    I am counting on you!

    Before I forget: What is your name rookie?\n
    """
    for character in setup_01:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.03) # gives delay to input of 5 miliseconds
    player_name = input("> ") # could directly write to myPlayer.name, but keep it seperated to eventually add functionality later
    myPlayer.name = player_name

    ### DIFFICULTY LEVEL LOD ###
    setup_02 = """

    Select your difficulty level!\n
    """
    setup_02_added = """
    (You can play on 'hard', 'medium' or 'easy')\n
    """
    for character in setup_02:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.03) # gives delay to input of 5 miliseconds
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
    

    #### STARTS GAME AFTER SETUP ####
    os.system("clear") 
    setup_03 = """

    Great!

    Let's get you started. There are already people lining up.\n
    """
    for character in setup_03:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.03) # gives delay to input of 5 miliseconds
    main_game_loop()

title_screen() # launches the game and setup