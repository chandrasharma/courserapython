# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if (name == "rock"):        
       return 0;
    elif (name == "paper"):
       return 1;
    elif (name == "scissors"):
       return 2;
    elif (name == "lizard"):
       return 3;
    elif (name=="Spock"):   
       return 4;
    else:
        "Please enter a valid name"

#print name_to_number("rock")
#print name_to_number("Spock")
#print name_to_number("paper")
#print name_to_number("lizard")
#print name_to_number("scissors")

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
   
    if number == 0:        
        return "rock"
        
    elif number == 1:
        return "paper"
    elif number == 2:
        return "scissor"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "Spock"
    else:
        print "please enter a number from 0-4"         
    

    
#print number_to_name(0)
#print number_to_name(1)
#print number_to_name(2)
#print number_to_name(3)
#print number_to_name(4)
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
def rpsls(player_choice): 
    print "\n"
    # delete the following pass statement and fill in your code below
    print "Player chooses " + player_choice
    
    player_number=name_to_number(player_choice)
    import random
    comp_number=random.randrange(0,4)
    comp_choice = number_to_name( comp_number );
    print "Computer chooses " + comp_choice
 
    difference = (comp_number - player_number) % 5
     
 
    if( difference == 1 or difference == 2 ):
        print "Computer wins!"
    elif ( difference == 4 or difference == 3 ):
        print "Player wins!"
    elif( difference == 0 ):
        print "Player and computer tie!"
         
            
 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
             
 
 



        
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE 

# always remember to check your completed program against the grading rubric


