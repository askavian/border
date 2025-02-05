# loaded_c03 = "c03 loaded successfully"  #debugging
# print(loaded_c03)

from run import time # imports the time remaining value from main
from run import score # imports the score value
from run import people_left # people left
c03_conclusion = None # Final Conclusion State for this case
c03_conclusion_good = "c03 GOOD OUTCOME"
c03_conclusion_bad = "c03 BAD OUTCOME"
c03_conclusion_secret = "c03 SECRET OUTCOME" # unused at the moment

c03_01 = str("""
             
        Name: tbd
        Date of Birth: tbd
        Place of Birth: tbd

        c03 OVERVIEW    
        XXXDUMMYTEXTXXX
             
        """)

print(c03_01)
print("You have " + str(time) + " minutes remaining.")

while c03_conclusion == None:
    c03_01_des = str(input("""
                       
        How do you want to proceed? 

          Make A Descision:                               
        "DENY"    the request for entry and send the individual back, or 
        "APPROVE" the request for entry and let the individual enter the Occupied Terretories.

          Further Investigate:                              
        "luggage" to examine his belongings, or
        "search"  to perform a full body search on the  the individual, or
        "question" to inquire about the reasons for enter. 
                       
        """))
    if c03_01_des == 'APPROVE':
        time = (time - 1) 
        score = score + 10 # TBD
        people_left = people_left - 1
        c03_conclusion = c03_conclusion_good
        print("""
        
        c03 APPROVE      
        XXXDUMMYTEXTXXX
        
        """)
    elif c03_01_des == 'DENY':
        time = (time - 2) 
        score = score + 1
        people_left = people_left -1
        c03_conclusion = c03_conclusion_bad
        print("""
        
        c03 DENY      
        XXXDUMMYTEXTXXX
        
        """)
    elif c03_01_des == 'search':
        time = (time - 10)
        print("""
        
        c03 search      
        XXXDUMMYTEXTXXX
                  
        """)
    elif c03_01_des == 'luggage':
        time = (time - 5) 
        print("""
        
        c03 luggage      
        XXXDUMMYTEXTXXX
                  
        """)
    elif c03_01_des == 'question':
        time = (time - 5) 
        print("""
        
        c03 question      
        XXXDUMMYTEXTXXX
                  
        """)
    else:
        time = (time - 10) 
        score = score + 5
        people_left = people_left -1
        c03_conclusion = c03_conclusion_bad
        print("""

        c03 else
        XXXDUMMYTEXTXXX
        
        """)
    
print(c03_conclusion) 
print(score) 

print("You have " + str(time) + " minutes remaining.")
