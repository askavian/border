# loaded_c01 = "c01 loaded successfully" #debugging
# print(loaded_c01)  

from run import time # imports the time remaining value from main
from run import score # imports the score value
from run import people_left # people left
c01_conclusion = None # Final Conclusion State for this case
c01_conclusion_good = "c01 GOOD OUTCOME"
c01_conclusion_bad = "c01 BAD OUTCOME"
c01_conclusion_secret = "c01 SECRET OUTCOME"

c01_01 = str("""
             
        Name: Abdul Rahim
        Date of Birth: Dec.11th 1999
        Place of Birth: Erbil, Iraq
             
        The passport was recently issued and shows no obvious signs of damage or manipulation. 
             
        You recognize the person in front of you as the same person shown on the passport photo. 
             
        The eyes are the same; the shape of the ears is the same and you recognize a birthmark beneath the left eye.

        However, in his passport, the person has a full beard and hair. The man in front of you is bald and fully shaven.
             
        """)

print(c01_01)
print("You have " + str(time) + " minutes remaining.")

while c01_conclusion == None:
    c01_01_des = str(input("""
                       
        How do you want to proceed? 

          Make A Descision:                               
        "DENY"    the request for entry and send the individual back, or 
        "APPROVE" the request for entry and let the individual enter the Occupied Terretories.

          Further Investigate:                              
        "luggage" to examine his belongings, or
        "search"  to perform a full body search on the  the individual, or
        "question" to inquire about the reasons for enter. 
                       
        """))
    if c01_01_des == 'APPROVE':
            time = (time - 1) 
            score = score + 1 # no modification
            people_left = people_left - 1
            c01_conclusion = c01_conclusion_bad
            print("""
        
        Abdul Rahim passes through the border crossing uninterrupted. 
          
        You missed the 2kg of C4 Abdul was carrying. 
          
        As you hear from the News later that evening, Abdul detonated the bomb he was carrying in a bus 
        en-route to the city, killing 15 people.
          
        You are a terrible Immigration Officer.
          
        You lose!
        
        """)
    elif c01_01_des == 'DENY':
            time = (time - 2) 
            score = score + 10
            people_left = people_left - 1
            c01_conclusion = c01_conclusion_good
            print("""
        
        Abdul Rahim is shouting about racial profiling and why you refuse him. 
              
        But ultimately he leaves the border crossing and returns.
        
        """)
    elif c01_01_des == 'search':
            time = (time - 10)
            score = score + 30
            people_left = people_left - 1
            c01_conclusion = c01_conclusion_secret # secret conclusion 
            print("""
        
        You perform a full check on Abdul and his belonging. 
                  
        You find 2kg of C4 inside a suicide vest underneath his shirt and a detailed list of a planned attack in the city.
                  
        Abdul is arrested!
                  
        """)
    elif c01_01_des == 'luggage':
            time = (time - 5) 
            print("""
        
        You go through Abdul's luggage and find:
          # A few personal belongings. Among them a picture of his family and a religious object. 
          # Clothing items that are in remarkable condition (brand new). But the amount of clothing seems off. There is only one
            pair of underwear, but five shirts and two pair of suit pants. 
          # No fluids, alcohol or any other contraband. 

          There is no contraband in Abdul's suitcase or any other illegal items.  
                  
        """)
    elif c01_01_des == 'question':
            time = (time - 5) 
            print("""
        
        At first, Abdul is hestitant to answer your questions, but after a while he opens up. 
          
        Abdul plans on staying at least two weeks in the city. 
          
        His plans are to search for his family that got seperated during the war. 
          
        Unfortunately, he has no place to stay yet and no Hotel Reservation. This is odd, because usually, people are booking 
        their accomodation way in advance within a secure Hotel with Security when visiting Argonia.  
                  
        """)
    else:
            time = (time - 10) 
            score = score + 5
            people_left = people_left - 1
            c01_conclusion = c01_conclusion_good # deny
            print("""
          
        Abdul gets bored and leaves after a while.
        
        """)
       
print(c01_conclusion) 
print(score)

print("You have " + str(time) + " minutes remaining.")

