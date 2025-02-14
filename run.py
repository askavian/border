# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


#  Welcome to:   
#
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
#  A game about tough moral choices and consequences.
#
#  by Malte M. Boettcher 


import sys  # imports system functions -> used here for "exit" command to close game
import os  # imports operating systems functions -> used "clear" command NOT "cls" for Heroku
import time  # imports time related functions -> used here for text output delay


#### PLAYER INITITAL SETUP ####

class player:
    def __init__(self):
        self.name = ""  # set by player input during setup
        self.lod = None  # Difficulty Level (hard, medium, easy)
        self.time = 0  # level hard = 30 min / medium = 45 min / easy = 60 min
        self.score = 0  # Score between 0 and 100 in the final assessment 
        self.people = 0  # people left in the queue, must be same number as cases in game
        self.currentcase = "c01"  # is set to the current case, always start wit c01
        self.game_over = False  # primary game condition
myPlayer = player()  # sets myPlayer to player class


#### TITLE SCREEN AND SETUP ####
# First thing to greed the player

def title_screen_selections():  # defines the options on the title screen
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()  # calls setup_game to begin game
    elif option.lower() == ("help"):
        help_menu()  # calls the help menu
    elif option.lower() == ("quit"):
        sys.exit()  # quits the game by exiting the application. To restart, restart the browser window
    while option.lower() not in ["play", "help", "quit"]:  # repeats valid options for error prevention
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game() 
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit() 

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

# Only accessible from start screen
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


#### CASES VARIABLES ####
# These variables define all values that are used in each case

case = "CASE"  # not in use bit remains in the code for organizational reasons
introduction = "INTRO"  # stores the introduction and main data. 
luggage = "LUGGAGE" #  to examine the belongings of an individual
luggagecondition = "LUGGCOND"  # can only be 0 or 3 and set if a secret outcome is here
search = "SEARCH"  # to stripsearch an individual
searchcondition = "SEARCOND"  # can only be 0 or 3 and set if a secret outcome is here
question = "QUESTION"  # to inquire about the reasons for enter 
questioncondition = "QUESCOND"  # can only be 0 or 3 and set if a secret outcome is here
approve = "APPROVE"  # approves the request and let the individual pass the border
approvecondition = "APPRCOND"  # can only be 1 (good) or 2 (bad) and set if a regular outcome is here
deny = "DENY"  # deny the entry request and prevents the individual from entering 
denycondition = "DENYCOND"  # can only be 1 (good) or 2 (bad) and set if a regular outcome is here
solved = "SOLVED"  # sets a boolean for if a case has already been closed, used for moving to a next case
condition = "CONDITION"  # 1 (good outcome), 2 (bad outcome), 3 (secret outcome) used for the final assessment
goodoutcome = "GOODOUT"  # text for good outcome for the final assessment
goodcondition = "GOODCOND"  # var for good outcome for the final assessment
badoutcome = "BADOUT"  # text for bad outcome for the final assessment
badcondition = "BADCOND"  # var for bad outcome for the final assessment
secretoutcome = "SECOUT"  # text for secret outcome for the final assessment
secretcondition = "SECCOND"  # var for secret outcome for the final assessment
nextcase = "NEXT"  # defines the next case in line after the current


#### CASEMAP ####
# as a key value map as defined above

casemap = {
    "c01": {
    case: "Lanto Blorg",

    introduction: """
    Name: Lanto Blorg
    Date of Birth: Dec.11th, 1999
    Sex: Male

    The passport was recently issued and shows no obvious signs of damage or
    manipulation.
    You recognize the person in front of you as the same person shown in the 
    photo.
    The eyes are the same, the shape of the ears is the same and you
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
      but five shirts and two pairs of suit pants.
    # No fluids, alcohol, or any other contraband.

    There is no contraband or any other illegal items in Lanto's suitcase.
    """,
    luggagecondition: 0,
    search: """
    You perform a full check on Lanto and his belongings.

    You find 2kg of C4 inside a suicide vest underneath his shirt and a
    detailed list of a planned attack in the city.

    Lanto is arrested!
    """,
    searchcondition: 3,
    question: """
    At first, Lanto is hesitant to answer your questions, but after a
    while he opens up.
    
    Lanto plans on staying in the city for at least two weeks.

    He plans to search for his family who got separated during the war.
    Unfortunately, he has no place to stay and no Hotel Reservation.
    This is odd, because usually, people are booking their accommodation
    way in advance within a secure Hotel with Security when visiting.
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
    He tried to cross the border but was rejected. On his way back home,
    the suicide vest went off but killing only him.
    """,
    goodcondition: False,
    badoutcome: """
    A Terrorist Attack happened on a public bus this afternoon, killing
    15 and injuring 7, including children.
    The individual was later identified as Lanto Blorg and was able to pass
    the border uninterrupted while carrying a suicide vest.
    """,
    badcondition: False,
    secretoutcome: """
    A Terrorist Attack was prevented today thanks to a new border guard
    officer on his first day of duty!
    While searching for the would-be terrorist, identified as Lanto Blorg,
    the guard noticed a suicide vest.
    The guard took immediate action and as such prevented a disaster.
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
    She wears full makeup (maybe a bit too much) and from the optics, she
    can be considered beautiful.

    Her behavior seems erratic, however, and while talking to you, she
    constantly looks over her shoulder.

    Maybe she is fleeing something.... or someone.
    """,
    luggage: """
    Dammyra's luggage is hastily thrown together. Crucial items are missing.

    There is no toothbrush and very few personal items besides clothing.

    You find a worn-out teddy bear and a picture of Dammyra at a much younger
    age with an older woman. Both women look happy.

    You find a small amount of Marihuana in a little plastic bag at the
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

    The injuries are not fresh. Maybe 4 days to 2 weeks old and in
    different stages of healing.

    You also find a name tattooed on her left thigh and her arms show heavy
    signs of substance abuse.

    This might be a mark of a pimp.
    """,
    searchcondition: 0,
    question: """
    Dammyra claims to be visiting her sister.

    While questioning Dammyra becomes nervous and gives answers that don't
    add up.
    The address she provides does not exist and she changed the name of her
    sister during the interview.

    After being called on it, she breaks and begins to cry and sob
    uncontrollably.

    She now claims to be going back home after being obducted 5 years ago
    by a group of human-traffickers.

    She was able to flee this morning.

    She might be lying but in the end, her story checks out and you hand her
    over to the authorities.
    """,
    questioncondition: 3,
    approve: """
    When you stamp her passport, you can see the relief on Dammyra's face.
    She passes the border uninterrupted.
    """,
    approvecondition: 1,
    deny: """
    Dammyra is visibly upset and frightened. She hesitates to walk back, but
    in the end, she gives up and leaves.
    """,
    denycondition: 2,
    solved: False,
    condition: 0,
    goodoutcome: """  
    A group of criminals roaming a neighborhood tonight was arrested by the
    police.
    When questioned the police found evidence that the group was looking for
    a young woman who was reported missing 5 years ago.
    The woman did not show up at home one night and was presumed dead.
    """,
    goodcondition: False,
    badoutcome: """
    A woman later identified as Dammyra de Brillaal was refused entry to the
    border today and was later found dead.
    Dammyra went missing from her parent's house five years ago and was
    presumed dead.
    Her body was found in a dumpster and showed obvious signs of violence.
    Our neighbor's police force is leading the investigation.
    """,
    badcondition: False,
    secretoutcome: """
    A woman missing for five years was reunited with her mother today. She
    was spüotted entering the country at the border and after showing signs
    of abuse was handed over to protection agencies.
    The police said that the information gathered by her could lead to a
    breakthrough in a human trafficking case in both countries.
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

    The passport is old and has only a few days until its expiration date.
    Usually, passports must be valid for at least 30 days at the point of
    entry.

    The passport marks Solomon as a member of the medical aid group.

    The Picture is quite dated. He has full hair and a beard, but you can
    see that the individual presenting to you is the same. But 10-15 years
    older.
    """,
    luggage: """
    During the search through Solomons's luggage, you find clothing,
    personal hygiene products, a notebook, and a few books on medicine.

    You also find a letter from the WHO recommending Solomon for work on
    the viral outbreak in the country after the war.

    You approve Solomon's Entry request regardless of his passport validity
    and give the Ministry of Health a call.

    The MoH is already expecting him and is sending a vehicle to pick him
    up right away.
    """,
    luggagecondition: 3,
    search: """
    Solomon is embarrassed by the search procedure.

    You find nothing of value.

    Just a naked old man.
    """,
    searchcondition: 0,
    question: """
    Solomon seems bothered by your questions and a bit annoyed.

    After a while, he claims to work for the World Health Organisation and
    he claims to be an expert virologist.

    He wants to help after the war.
    """,
    questioncondition: 0,
    approve: """
    You approve Solomons's entry request and he slowly walks to the taxis
    waiting outside.
    """,
    approvecondition: 1,
    deny: """
    You deny Solomons's request for entry. He seems irritated by that, but
    after a short while, he says: 'Fine. I go on vacation. I don't like
    being here anyway.' and walks away.
    """,
    denycondition: 2,
    solved: False,
    condition: 0,
    goodoutcome: """
    The famous WHO Virologist: Dr. Solomon Candlegorn arrived today in our
    glorious nation to help with a violent outbreak in the most devestated
    parts of the country. Unfortunately, Dr. Candelgorn was stuck in traffic
    so he wasn't able to begin work right away. This may lead to some more
    people getting infected.
    """,
    goodcondition: False,
    badoutcome: """
    The famous WHO Virologist: Dr. Solomon Candlegorn was scheduled to arrive
    today in our glorious nation but was held up and refused entry by a new
    guard at the border. It is unclear when he will be able to visit again
    because he is currently missing. This might lead to a significant
    outbreak or even a pandemic.
    """,
    badcondition: False,
    secretoutcome: """
    The famous WHO Virologist: Dr. Solomon Candlegorn arrived today at our
    glorious nation to help with a violent outbreak in the most devastated
    parts of the country. A Rookie Border Guard spotted the famous scientist
    and fast-tracked his entry so he was able to avoid traffic and get to
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
    the woman presenting to you. But the passport shows signs of damage and
    some stains that look like blood.

    Adettel looks roughed up. A woman who is obviously fond of hard labor
    and doesn't use make-up very often. She wears a bandana and work-out
    old military clothing.

    You recognize Adettel from somewhere. Maybe an old school acquaintance
    or someone on TV.

    You cannot tell.
    """,
    luggage: """
    Adettel is visibly uncomfortable while you are going through her case.

    You find a few dirty clothes and personal hygiene items.

    Wrapped in old rags you find leaflets and something that looks like
    a political manifest that Adettel seems to be the author of.
    On closer inspection, you realize the items are communist
    propaganda.

    Owning propaganda is not illegal, but now you realize where you have
    seen Adettel before. During the war, she led a guerilla group and was
    responsible for horrible war crimes.

    You arrest Adettel and hand her over to the Police.

    Adettel curses you on her way out in handcuffs.
    """,
    luggagecondition: 3,
    search: """
    Adettel makes some snarky remarks while you search her. But she is not
    resisting.

    It is probably not the first time for her.

    She has old scars and bruises all over her body.
    """,
    searchcondition: 0,
    question: """
    Adettel claims to be visiting friends and family.

    The addresses and the hotel she booked for herself check out positive.

    Her story seems to be correct.
    """,
    questioncondition: 0,
    approve: """
    Adettel looks at you with a cold gaze for a light moment and then
    nods and passes the border.
    """,
    approvecondition: 2,
    deny: """
    Adettel is angry after being rejected. She is not willing to leave but
    after being forced out by two officers the finally gives up and leaves.
    """,
    denycondition: 1,
    solved: False,
    condition: 0,
    goodoutcome: """
    The infamous Communist Gurellia Gang "The Red Sun" is losing support
    in both nations. Adettel Hovelweir, leader of the gang a most-wanted
    is still at large, but the group seems to be unable to gain a foothold
    in new territory since the war ended.
    """,
    goodcondition: False,
    badoutcome: """
    Today, leaflets and propaganda material from the infamous guerilla gang
    "The Red Sun" surfaced on the streets of our glorious nation. Adettel
    Hovelweir, leader of the group and one of the most wanted terrorists in
    both nations was briefly spotted on the streets of the capital.
    """,
    badcondition: False,
    secretoutcome: """
    The infamous Adettel Hovelweir, leader of the communist Gurellia Force
    "The Red Sun" was caught today at the border by a young officer. The
    group was responsible for numerous war crimes, including terror attacks.
    """,
    secretcondition: False,
    nextcase: "c05",
    },
    "c05": {
    case: "Aspermeia van der Grim",
    introduction: """
    Name: Aspermeia van der Grim
    Date of Birth: March.19th, 1951
    Sex: Female

    The passport is temporary and identifies Aspermeia as an early refugee.

    The picture in the passport shows Aspermeia in her younger years, but it
    is her.
    """,
    luggage: """
    Old clothing, old photos, and memorabilia.

    You find some gold statues and valuables that might have value, but you
    can see, that it is very personal. An old necklace with a picture
    catches your eye. It shows a much younger version of Aspermeia with a
    young officer.
    After thinking about it for a while, you realize the officer is General
    Elam Al Shaabaai, is a famous war hero of our nation. But you don't recall
    whether he is alive or dead.

    You find also some heart medicine and pain medication.
    The pain medication counts as a drug and cannot be imported without a
    license. A license, that Aspermeia doesn't have.
    """,
    luggagecondition: 0,
    search: """
    Aspermeia is embarrassed by the search procedure.

    You find nothing of value.
    
    Just a naked old lady.
    """,
    searchcondition: 0,
    question: """
    Aspermeia breaks in tears while you are questioning her.

    She was away from home for too long. She is sick and came here to live
    the remainder of her life in peace.

    After all these years, she wants to see who is still alive in her town.

    She wants to find her Brother Elam and his family.

    You let her pass and give her the way to the NGO that helps refugees
    to connect with lost loved ones.

    Aspermeia is grateful that you approved her request and promises to
    bring you a cake in the coming days.
    """,
    questioncondition: 3,
    approve: """
    Aspermeia is grateful that you approved her entry request and thanks
    you on her way into the country.
    """,
    approvecondition: 1,
    deny: """
    Aspermeia is devastated and doesn't know what to do now.
    She staggers towards the exit leading back and breaks down in tears.
    """,
    denycondition: 2,
    solved: False,
    condition: 0,
    goodoutcome: """
    Aspermeia van der Grim, the sister of General Elam Al Shaabaai returned
    home today after living and helping in a refugee camp for the past 20
    years. Her family is taking good care of her.
    """,
    goodcondition: False,
    badoutcome: """
    Aspermeia van der Grim, the sister of General Elam Al Shaabaai sufferd
    a fatal heart attack today on the side of a road after being refused
    entry into our glorious nation.
    """,
    badcondition: False,
    secretoutcome: """
    Aspermeia van der Grim, the sister of General Elam Al Shaabaai returned
    home today after living and helping in a refugee camp for the past 20
    years. She has been a beacon of hope for refugees and a voice of reason
    and understanding between both of our nations.
    """,
    secretcondition: False,
    nextcase: "",
    },
}
#### GAME INTERACTIVITY ####
def print_currentcase():  # This function prints the current case from the casemap 
    print("\n" + ("#" * (4 + len(myPlayer.currentcase))))
    print("REQUEST FOR ENTRY: ")
    speech = casemap[myPlayer.currentcase] [introduction]
    for character in speech:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.001)  # this is very short due to this section being repeated 

def prompt():  # function prompts all the available answers in each case
    print("\n" + "===================")
    print("go through 'luggage', 'question' the individual, 'search' the individual, 'deny' or 'approve' the entry")
    print("What would you like to do?\n")
    action = input("> ")
    acceptable_actions = ["luggage", "search", "question", "approve", "deny", "quit"]
    while action.lower() not in acceptable_actions:
        print("That is not a valid Action\n")
        action = input("> ")
    if action.lower() == "quit":  # exits the application at any time
        print("Goodbye! Reload the Game to try again.")
        sys.exit()
    elif action.lower() == "luggage":
        player_luggage(action.lower())  # calls the player_luggage function when answer is typed in
    elif action.lower() == "search":
        player_search(action.lower())  # calls the player_search function when answer is typed in
    elif action.lower() == "question":
        player_question(action.lower())  # calls the player_question function when answer is typed in
    elif action.lower() == "deny":
        player_deny(action.lower())  # calls the player_deny function when answer is typed in
    elif action.lower() == "approve":
        player_approve(action.lower())  # calls the player_approve function when answer is typed in

def player_luggage(action):  # calls the "luggage" answer when typed in above
    myPlayer.time = myPlayer.time - 8
    speech = casemap[myPlayer.currentcase] [luggage]
    for character in speech:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2.5)
    if casemap[myPlayer.currentcase] [luggagecondition] == 3:
        casemap[myPlayer.currentcase] [condition] = 3
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [secretcondition] = True
        player_nextcase()  # if statement checks if a secret ending is here and calls player_nextcase

def player_search(action):  # calls the "search" answer when typed in above
    myPlayer.time = myPlayer.time - 12
    speech = casemap[myPlayer.currentcase] [search]
    for character in speech:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2.5)
    if casemap[myPlayer.currentcase] [searchcondition] == 3:
        casemap[myPlayer.currentcase] [condition] = 3
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [secretcondition] = True
        player_nextcase()  # if statement checks if a secret ending is here calls player_nextcase

def player_question(action):  # calls the "question" answer when typed in above
    myPlayer.time = myPlayer.time - 5
    speech = casemap[myPlayer.currentcase] [question]
    for character in speech:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2.5)
    if casemap[myPlayer.currentcase] [questioncondition] == 3:
        casemap[myPlayer.currentcase] [condition] = 3
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [secretcondition] = True
        player_nextcase()   # if statement checks if a secret ending is here and calls player_nextcase

def player_approve(action):  # calls the "approve" answer when typed in above
    myPlayer.time = myPlayer.time - 1
    speech = casemap[myPlayer.currentcase] [approve]
    for character in speech:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2.5)
    if casemap[myPlayer.currentcase] [approvecondition] == 1:
        casemap[myPlayer.currentcase] [condition] = 1
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [goodcondition] = True
        player_nextcase()  # if statement checks if a good ending is here and calls player_nextcase
    elif casemap[myPlayer.currentcase] [approvecondition] == 2:
        casemap[myPlayer.currentcase] [condition] = 2
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [badcondition] = True
        player_nextcase()  # elif statement checks if a bad ending is here and calls player_nextcase

def player_deny(action):  # calls the "deny" answer when typed in above
    myPlayer.time = myPlayer.time - 2
    speech = casemap[myPlayer.currentcase] [deny]
    for character in speech:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2.5)
    if casemap[myPlayer.currentcase] [denycondition] == 1:
        casemap[myPlayer.currentcase] [condition] = 1
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [goodcondition] = True
        player_nextcase()  # if statement checks if a good ending is here and calls player_nextcase
    elif casemap[myPlayer.currentcase] [denycondition] == 2:
        casemap[myPlayer.currentcase] [condition] = 2
        casemap[myPlayer.currentcase] [solved] = True
        casemap[myPlayer.currentcase] [badcondition] = True
        player_nextcase()  # elif statement checks if a bad ending is here and calls player_nextcase


def player_nextcase():  # moves player to next case by updating myPlayer.currentcase to value of nextcase
    os.system("clear")  # clears the screen for the next case
    myPlayer.people = myPlayer.people - 1  # deducts myPlayer.people by one
    if myPlayer.people == 0:  # if statement if myPlayer.people reaches 0
        endspeech = "Your shift ended Rookie.\n"
        endspeech = "You can go home now. Get some rest.\n"
        for character in endspeech:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        final()  # moves to final for finas assessment and ending
    else:  # else statement if number of people is greater than 0
        myPlayer.currentcase = casemap[myPlayer.currentcase] [nextcase]


#### FINAL ASSESSMENT ####
def final():  # produces the final assessment for ending the game
   time.sleep(2.5)
   newsspeech = """

   \n   Welcome to today's Evening News!   \n
   
   """  # prints the final assessment in form of a news article
   for character in newsspeech:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   print("""
                  
         """)
   if casemap["c01"] [condition] == 3:  # ALL if/elif statements are checking the individual outcomes of cases
       myPlayer.score = myPlayer.score + 20  # stores the respective point value in myPlayer.score for final score
       c01sec = casemap["c01"] [secretoutcome] +"\n"  # prints the outcome of a case based on conditions above
       for character in c01sec:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   elif casemap["c01"] [condition] == 1:
       myPlayer.score = myPlayer.score + 10
       c01goo = casemap["c01"] [goodoutcome] +"\n"
       for character in c01goo:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   elif casemap["c01"] [condition] == 2:
       myPlayer.score = myPlayer.score + 1
       c01bad = casemap["c01"] [badoutcome] +"\n"
       for character in c01bad:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   if casemap["c02"] [condition] == 3:
       myPlayer.score = myPlayer.score + 20
       c02sec = casemap["c02"] [secretoutcome] +"\n"
       for character in c02sec:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   elif casemap["c02"] [condition] == 1:
       myPlayer.score = myPlayer.score + 10
       c02goo = casemap["c02"] [goodoutcome] +"\n"
       for character in c02goo:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   elif casemap["c02"] [condition] == 2:
       myPlayer.score = myPlayer.score + 1
       c02bad = casemap["c02"] [badoutcome] +"\n"
       for character in c02bad:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   if casemap["c03"] [condition] == 3:
       myPlayer.score = myPlayer.score + 20
       c03sec = casemap["c03"] [secretoutcome] +"\n"
       for character in c03sec:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   elif casemap["c03"] [condition] == 1:
       myPlayer.score = myPlayer.score + 10
       c03goo = casemap["c03"] [goodoutcome] +"\n"
       for character in c03goo:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   elif casemap["c03"] [condition] == 2:
       myPlayer.score = myPlayer.score + 1
       c03bad = casemap["c03"] [badoutcome] +"\n"
       for character in c03bad:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   if casemap["c04"] [condition] == 3:
       myPlayer.score = myPlayer.score + 20
       c04sec = casemap["c04"] [secretoutcome] +"\n"
       for character in c04sec:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   elif casemap["c04"] [condition] == 1:
       myPlayer.score = myPlayer.score + 10
       c04goo = casemap["c04"] [goodoutcome] +"\n"
       for character in c04goo:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   elif casemap["c04"] [condition] == 2:
       myPlayer.score = myPlayer.score + 1
       c04bad = casemap["c04"] [badoutcome] +"\n"
       for character in c04bad:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   if casemap["c05"] [condition] == 3:
       myPlayer.score = myPlayer.score + 20
       c05sec = casemap["c05"] [secretoutcome] +"\n"
       for character in c05sec:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   elif casemap["c05"] [condition] == 1:
       myPlayer.score = myPlayer.score + 10
       c05goo = casemap["c05"] [goodoutcome] +"\n"
       for character in c05goo:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   elif casemap["c05"] [condition] == 2:
       myPlayer.score = myPlayer.score + 1
       c05bad = casemap["c05"] [badoutcome] +"\n"
       for character in c05bad:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   print("""
        \n
         """)
   newsspeech = """

   \n Officer """ + myPlayer.name + """. You scored """ + str(myPlayer.score) + """ out of 100.\n

   """
   for character in newsspeech:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


   time.sleep(10)  # prevents the game from closing for 60 seconds, to give time read the outcome
   myPlayer.game_over = True  # closes the game loop


#### GAME FUNCTIONALITY ####
def main_game_loop():  # main gameloop bring the player always back to the current
    while myPlayer.game_over is False:
        print("""
            
              You have """ + str(myPlayer.time) + """ minutes remaining until the end of your shift!\n
              
              """)  # displays the remaining time to the player after each action
        print_currentcase()  # prints the myPlayer.currencase from the casemap
        prompt()  # if time reaches 0 the myPlayer.game_over is triggered and the game is lost
        if myPlayer.time < 0:  # FAILING CONDITION "run out of time"
            myPlayer.game_over
            print("""
                  You shift ended and there are still people waiting.
                  
                  You Lost!""")
            sys.exit()  # closes the game


#### SETUP ####

def setup_game():  # initial setup function to set the tone and set name and lod
    os.system("clear")

    ### NAME ###
    setup_01 = """
    Welcome to the border rookie!

    We have fought a long and bloody war against our neighbors and a lot of
    good people died!

    But thanks to the might of our army and our glorious overlords we won!

    The situation on the border now is stable, but don't be fooled! Even the
    tiniest spark can reignite hostilities.
    There are religious zealots, political extremists and criminals trying
    to seize the opportunity. Contraband Items, Weapons, Human-Traffiking, we
    got it all!
    There are also a lot of great folks out here. Folks that we need to let
    in. Aid workers, Refugees, displaced people, and folks that are simply
    looking for a way home.

    If we want to have a bright future with our neighbors, we have to make
    this work!.

    I am counting on you!

    Before I forget: What is your name rookie?\n
    """
    for character in setup_01:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)  # gives delay to input of 5 miliseconds
    player_name = input("> ")
    myPlayer.name = player_name  # stores the player name

    ### DIFFICULTY LEVEL LOD ###
    # the difficulty level can be chosen here
    setup_02 = """

    Select your difficulty level!\n
    """
    setup_02_added = """
    (You can play on 'hard', 'medium' or 'easy')\n
    """
    for character in setup_02:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)  # gives delay to input of 5 miliseconds
    for character in setup_02_added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)  # gives delay to input of 1 miliseconds
    player_lod = input("> ")
    valid_lod = ["hard", "medium", "easy"] # list of only valid values that are accepted for error prevention 
    if player_lod.lower() in valid_lod:
        myPlayer.lod = player_lod
    while player_lod.lower() not in valid_lod:
        player_lod = input("> ")
        if player_lod.lower() in valid_lod:
            myPlayer.lod = player_lod


    #### PLAYER STATS ####
    if myPlayer.lod == "hard":  # the LoD sets the remaining time for the player
        myPlayer.time = 30
        myPlayer.people = 5 # Equal to the number of cases maybe used for LoD later
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
    """  # final setup functions as a soft handover to the main_game_loop
    for character in setup_03:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)  # gives delay to input of 5 miliseconds
    main_game_loop()

title_screen()  # launches the titel_screen is called first when the game starts