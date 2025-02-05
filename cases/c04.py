# loaded_c04 = "c #debugging04 loaded successfully"
# print(loaded_c04)

from run import time # imports the time remaining value from main
from run import score # imports the score value
from run import people_left # people left
c04_conclusion = None # Final Conclusion State for this case
c04_conclusion_good = "c04 GOOD OUTCOME"
c04_conclusion_bad = "c04 BAD OUTCOME"
c04_conclusion_secret = "c04 SECRET OUTCOME" # unused at the moment

c04_01 = str("""
             
        Name: tbd
        Date of Birth: tbd
        Place of Birth: tbd

        c04 OVERVIEW    
        XXXDUMMYTEXTXXX
             
        """)

print(c04_01)
print("You have " + str(time) + " minutes remaining.")

while c04_conclusion == None:
    c04_01_des = str(input("""
                       
        How do you want to proceed? 

          Make A Descision:                               
        "DENY"    the request for entry and send the individual back, or 
        "APPROVE" the request for entry and let the individual enter the Occupied Terretories.

          Further Investigate:                              
        "luggage" to examine his belongings, or
        "search"  to perform a full body search on the  the individual, or
        "question" to inquire about the reasons for enter. 
                       
        """))
    if c04_01_des == 'APPROVE':
        time = (time - 1) 
        score = score + 10 # TBD
        people_left = people_left - 1
        c04_conclusion = c04_conclusion_good
        print("""
        
        c04 APPROVE      
        XXXDUMMYTEXTXXX
        
        """)
    elif c04_01_des == 'DENY':
        time = (time - 2) 
        score = score + 1
        people_left = people_left - 1
        c04_conclusion = c04_conclusion_bad
        print("""
        
        c04 DENY      
        XXXDUMMYTEXTXXX
        
        """)
    elif c04_01_des == 'search':
        time = (time - 10)
        print("""
        
        c04 search      
        XXXDUMMYTEXTXXX
                  
        """)
    elif c04_01_des == 'luggage':
        time = (time - 5) 
        print("""
        
        c04 luggage      
        XXXDUMMYTEXTXXX
                  
        """)
    elif c04_01_des == 'question':
        time = (time - 5) 
        print("""
        
        c04 question      
        XXXDUMMYTEXTXXX
                  
        """)
    else:
        time = (time - 10) 
        score = score + 5
        people_left = people_left -1
        c04_conclusion = c04_conclusion_bad
        print("""

        c04 else
        XXXDUMMYTEXTXXX
        
        """)
    
print(c04_conclusion) 
print(score) 

print("You have " + str(time) + " minutes remaining.")