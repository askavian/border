# loaded_c05 = "c05 loaded successfully"  #debugging
# print(loaded_c05)

from run import time # imports the time remaining value from main
from run import score # imports the score value
from run import people_left # people left
c05_conclusion = None # Final Conclusion State for this case
c05_conclusion_good = "c05 GOOD OUTCOME"
c05_conclusion_bad = "c05 BAD OUTCOME"
c05_conclusion_secret = "c05 SECRET OUTCOME" # unused at the moment

c05_01 = str("""
             
        Name: tbd
        Date of Birth: tbd
        Place of Birth: tbd

        c05 OVERVIEW    
        XXXDUMMYTEXTXXX
             
        """)

print(c05_01)
print("You have " + str(time) + " minutes remaining.")

while c05_conclusion == None:
    c05_01_des = str(input("""
                       
        How do you want to proceed? 

          Make A Descision:                               
        "DENY"    the request for entry and send the individual back, or 
        "APPROVE" the request for entry and let the individual enter the Occupied Terretories.

          Further Investigate:                              
        "luggage" to examine his belongings, or
        "search"  to perform a full body search on the  the individual, or
        "question" to inquire about the reasons for enter. 
                       
        """))
    if c05_01_des == 'APPROVE':
        time = (time - 1) 
        score = score + 10 # TBD
        people_left = people_left - 1
        c05_conclusion = c05_conclusion_good
        print("""
        
        c02 APPROVE      
        XXXDUMMYTEXTXXX
        
        """)
    elif c05_01_des == 'DENY':
        time = (time - 2) 
        score = score + 1
        people_left = people_left - 1
        c05_conclusion = c05_conclusion_bad
        print("""
        
        c05 DENY      
        XXXDUMMYTEXTXXX
        
        """)
    elif c05_01_des == 'search':
        time = (time - 10)
        print("""
        
        c05 search      
        XXXDUMMYTEXTXXX
                  
        """)
    elif c05_01_des == 'luggage':
        time = (time - 5) 
        print("""
        
        c05 luggage      
        XXXDUMMYTEXTXXX
                  
        """)
    elif c05_01_des == 'question':
        time = (time - 5) 
        print("""
        
        c05 question      
        XXXDUMMYTEXTXXX
                  
        """)
    else:
        time = (time - 10) 
        score = score + 5
        people_left = people_left -1
        c05_conclusion = c05_conclusion_bad
        print("""

        c05 else
        XXXDUMMYTEXTXXX
        
        """)
    
print(c05_conclusion) 
print(score) 

print("You have " + str(time) + " minutes remaining.")