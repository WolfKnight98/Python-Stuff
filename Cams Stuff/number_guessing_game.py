#Number Guessing Game#

# Import modules
import random

# Define variables
trys = 0
number = random.randint(0,11)

# Intro
print("Welcome to Cameron's number guessing game!")
print("I'm thinking of a number between 1 and 10, what number is it?")
while trys < 3:
    user = int(input("Have a guess: "))
    if user == number:
        print("Well done you guessed correctly!")
        print("Game over")
        break
    elif user < number:
        print("Guess higher next time")
        trys = trys + 1
    elif user > number:
        print("Guess lower next time")
        trys = trys + 1

if trys == 3:
    print("Game over!")
    print("The number was", number) 
