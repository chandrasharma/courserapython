# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random 
import sys

high=100
low=0
remaining_gusses100=7
remaining_gusses1000=10

# helper function to start and restart the game
def new_game(lo,hi):
 
    global secret_number, remaining_gusses100, high, low
    low=lo
    high=hi
    secret_number=random.randrange(low,high)  
    secret_number=float (secret_number)
    #print high,low
    #print secret_number

# define event handlers for control panel
def range100(): 
    global remaining_gusses100
    remaining_gusses100=7
    print ""
    print "New game. Range is from 0 to100" 
    print "Number of remaining gusses is:",remaining_gusses100
    print ""
    #print ""
    #guess = None 
    new_game(0,100)
def range1000(): 
    remaining_gusses1000=10
    print ""
    print "New game. Range is from 0 to1000"
    print "Number of remaining guesses is 10.0"
    print ""
    new_game(0,1000)  
def input_guess(guess):
    # main game logic goes here	     
    global remaining_gusses100,remaining_gusses1000, high, low
    player_guess = float(guess)
    print ""
    print "guess was :", player_guess
     
    if high==100.0:
       remaining_gusses100-=1 
       print "Number of remaining gusses is:", remaining_gusses100
       #print high, low
    else:
        high==1000.0
        remaining_gusses1000-=1 
        print "Number of remaining gusses is:", remaining_gusses1000
        #print "Number of remaining gusses is:", remaining_gusses100
   
    if high==100.0 and player_guess>100.0:
            print ""
            print "Please enter a value between 0 and 100"
            print "or click the button 0-1000 for bigger range"        
            remaining_gusses100=7
            print "Number of remaining gusses is :", remaining_gusses100
    elif high==1000.0 and player_guess>1000.0:
        print ""
        print "Please enter a value between 0 and 1000"        
        remaining_gusses1000=10 
        print "Number of remaining gusses is :", remaining_gusses1000

    elif high==100.0 and remaining_gusses100 == 0:    
       remaining_gusses100 = 7
       print ""
       print "New game. Range is from 0 to100" 
       print "Number of remaining gusses is:",remaining_gusses100
        
    elif high==1000.0 and remaining_gusses1000 == 0:    
       remaining_gusses1000 = 10
       print ""
       print "New game. Range is from 0 to1000" 
       print "Number of remaining gusses is:",remaining_gusses1000
        
    elif player_guess > secret_number:  
        #print secret_number
        print "Higher!" 
         
        new_game(low,high)
    elif player_guess < secret_number:
        #print secret_number
        print "Lower!"
        print ""
        new_game(low,high)
    elif player_guess == secret_number:
        print secret_number
        print "Correct!"    
        print ""
        new_game(low,high)        
    else:
        return""
    

     
# create frame
f = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
f.add_button("Range is (0-100)", range100, 200)
f.add_button("Range is (0-1000)", range1000, 200)
f.add_input("Enter number", input_guess, 100)
 
new_game(0,100)


# always remember to check your completed program against the grading rubric
