# Dan's number guessing game

# Import modules
import random

# Intro
print("Welcome to Dan's number guessing game!\n")

# Define variables
guesses = 0
number = random.randint(0, 10)

# Main program loop
while( guesses < 3 ):
    u_guess = int(input("Have a guess: "))

    if u_guess == number:
        print("Well done, you win!")
        break
    elif u_guess > number:
        print("Your guess was too high.")
        guesses = guesses + 1
    elif u_guess < number:
        print("Your guess was too low.")
        guesses = guesses + 1
    else:
        print("There was an error.")

if guesses == 3:
    print("You lose!")
    print("The number was: " + str(number))