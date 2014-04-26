# Basic command line clock by Dan
# Free to use and modifiy!

# Import modules
import os, time

# Define our time variables
hour = 0
minute = 0
second = 0

# While the second variable is less than 60
while second <= 60:

    # Clear Python CMD
    os.system( 'cls' )

    # Print the time with an integer format
    print( "%i:%i:%i" % ( hour, minute, second ) )

    # Sleep for 1 second
    time.sleep( 1 )

    # Add 1 to the second variable
    second += 1

    # If second is 60 then add 1 to the minute
    # variable and reset the second variable
    if second == 60:
        minute += 1
        second = 0

    # If minute is 60 then add 1 to the hour
    # variable and reset the minute and second variable
    elif minute == 60:
        hour += 1
        minute = 0
        second = 0
