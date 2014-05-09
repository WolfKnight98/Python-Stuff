# Atm, work in progress
# I did make a non-class version which I'll add soon
# Protected under the go forth and multiply you code stealing cake license

import random, os, subprocess
from atm_data import *

# The convention in python is that unchaging global variables should be all capitals
STARTING_BALANCE = 0
MAX_DEPOSIT = 500
MAX_WITHDRAW = 1000

# The ATM Class
class atm:

    # This function runs automatically when you call atm( str "Name", int pinCode )
    def __init__( self, name, pincode ):

        # Declare class variables from the function
        self.name = name
        self.pincode = pincode
        user_name, user_pincode = "", None

        # Ask the user to type there name
        user_name = str( input( "Type your name: " ) )

        if user_name != self.name:
            print( "Invalid name.", "\n" )
            user_name = False
        elif user_name == self.name:
            print( "Valid name.", "\n" )
            user_name = True
        self.idle_close_dialog()

        try:
            user_pincode = int( input( "Type your pincode: " ) )
        except ValueError:
            print( error, "\n" )
            exit()

        if user_pincode != self.pincode:
            print( "Invalid pincode.", "\n" )
            user_pincode = False
        elif user_pincode == self.pincode:
            print( "Valid pincode.", "\n" )
            user_pincode = True
        self.idle_close_dialog()

        if user_name and user_pincode == True:
            print( "Valid user and pincode, booting system.", "\n" )
            self.main_menu()
        else: 
            print( "Invalid user and pincode.", "\n" )
        self.idle_close_dialog()

    def idle_close_dialog( self ):
        """
        When using Idle input() creates a dialog that's polite to close after it's been used.
        But this program can be used directly from the command line too, without Idle, in which,
        trying to close the dialog outputs an unecessary error.
        """
        # This basically suppresses all output from calls to os.system()
        with open( os.devnull, "w" ) as fnull:
            result = subprocess.call( 'cls', stdout = fnull, stderr = fnull, shell = True )

    def main_menu( self ):
        balance = STARTING_BALANCE
        closing = False

        while not closing:
            for line in menu:
                print( line )
            print( "Your balance is £%i" % ( balance ) )

            user_menu_choice = int( input( " >>>  " ) )

            if user_menu_choice == 1:
                print( "You are eligible to withdraw a maximum of %i pounds." % ( MAX_WITHDRAW ), "\n" )

                try:
                    user_withdraw = int( input( "How much would you like to withdraw?\n >>>  " ) )
                except ValueError:
                    print( error )

                if user_withdraw > balance or user_withdraw > MAX_WITHDRAW:
                    print( "You can only withdraw %i pounds." % ( MAX_WITHDRAW ), "\n" )
                elif user_withdraw <= 0:
                    print( "Invalid funds specified.", "\n" )
                else:
                    print( "Funds deducted.", "\n" )
                    balance = balance - user_withdraw

            elif user_menu_choice == 2:
                print ( "You are eligible to deposit a maximum of %i pounds." % ( MAX_DEPOSIT ), "\n" )

                try:
                    user_deposit = int( input( "How much would you like to deposit?\n >>>  " ) )
                except ValueError:
                    print( error )

                if user_deposit > MAX_DEPOSIT:
                    print( "You can only deposit a maximum of %i pounds." % ( MAX_DEPOSIT ), "\n" )
                else:
                    print( "Funds added.", "\n" )
                    balance = balance + user_deposit

            elif user_menu_choice == 3:
                print( "Goodbye %s." % ( self.name ), "\n" )
                break

            self.idle_close_dialog()

if __name__ == "__main__":
    atm( "Dan", 1234 )