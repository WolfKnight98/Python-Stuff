# Dan's number guessing game

# Import modules
import random

# Define variables
guesses = 0
allowed_guesses = 3
number = random.randint( 0, 10 )

# Intro
print( "Welcome to Dan's number guessing game!\n" )

# Main program loop
while( guesses < 3 ):
    guess = input(
        "Choose a number between 0 and 10 (%s guesses remaining): " % ( allowed_guesses - guesses )
    )
    u_guess = int( guess )

    if u_guess == number:
        print( "OMG, how did you guess, you win and are cool!" )
        break
    elif u_guess > number:
        print( "Your guess was too high." )
        guesses = guesses + 1
    elif u_guess < number:
        print( "Your guess was too low." )
        guesses = guesses + 1
    else:
        print( "There was an error." )

if guesses == allowed_guesses:
    print( "You lose!" )
    print( "The number was: " + str( number ) )