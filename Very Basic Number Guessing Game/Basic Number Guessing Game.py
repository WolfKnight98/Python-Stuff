# Very basic number guessing game by Dan 

# Import modules
import random as r

# Define variables
randomNumber = r.randint( 1, 10 )
allowedGuesses = 3
guesses = 0

# run this loop while the user has enough guesses
while ( guesses < 3 ):

    # Ask the user to guess a number and notify them of how many guesses they have left
    guess = int( input( "Have a guess ( %s guesses remaining ) >>  " % ( allowedGuesses - guesses ) ) )

    # If the guess the user has made is equal to the random number
    if guess == randomNumber: 

        # Cheer them
        print( "Well done, you got it!" )

        # Break from the loop
        break

    # If the guess the user has made isn't the random number
    elif guess != randomNumber: 

        # Don't cheer them
        print( "That wasn't it." )

        # Add one guess
        guesses = guesses + 1

if guesses == allowedGuesses: print( "You lose, I win ahaha." )