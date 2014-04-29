# Atm, work in progress
# I did make a non-class version which I'll add soon
# Protected under the go forth and multiply you code stealing cake license
# Uncomment the time.sleeps and os.system( 'cls' )s for a nicer feel:D

import random, time, os
from atm_data import *

class atm:

    def __init__( self, name, pincode ):
        self.name = name
        self.pincode = pincode
        user_name, user_pincode = "", None

        user_name = str( input( "Type your name: " ) )

        if user_name != self.name:
            print( "Invalid name.", "\n" )
            user_name = False
        elif user_name == self.name:
            print( "Valid name.", "\n" )
            user_name = True
        os.system( 'cls' )

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
        os.system( 'cls' )

        if user_name and user_pincode == True:
            print( "Valid user and pincode, booting system.", "\n" )
            self.main_menu( 0, 1000, 500 )
        else: 
            print( "Invalid user and pincode.", "\n" )
        os.system( 'cls' )

    def main_menu( self, balance, max_withdraw, max_deposit ):
        self.balance = balance
        self.max_withdraw = max_withdraw
        self.max_deposit = max_deposit
        closing = False

        while not closing:
            for line in menu:
                print( line )

            user_menu_choice = int( input( " >>>  " ) )

            if user_menu_choice == 1:
                print( "Your balance is:", self.balance, "\n" )

            elif user_menu_choice == 2:
                print( "You are eligible to withdraw a maximum of %i pounds." % ( self.max_withdraw ), "\n" )

                try:
                    user_withdraw = int( input( "How much would you like to withdraw?\n >>>  " ) )
                except ValueError:
                    print( error )

                if user_withdraw > balance or user_withdraw > self.max_withdraw:
                    print( "You can only withdraw %i pounds." % ( max_withdraw ), "\n" )
                elif user_withdraw <= 0:
                    print( "Invalid funds specified.", "\n" )
                else:
                    print( "Funds deducted.", "\n" )
                    self.balance = self.balance - user_withdraw

            elif user_menu_choice == 3:
                print ( "You are eligible to deposit a maximum of %i pounds." % ( self.max_deposit ), "\n" )

                try:
                    user_deposit = int( input( "How much would you like to deposit?\n >>>  " ) )
                except ValueError:
                    print( error )

                if user_deposit > self.max_deposit:
                    print( "You can only deposit a maximum of %i pounds." % ( self.max_deposit ), "\n" )
                else:
                    print( "Funds added.", "\n" )
                    self.balance = self.balance + user_deposit

            elif user_menu_choice == 4:
                print( "Goodbye %s." % ( self.name ), "\n" )
                closing = True

            input()
            os.system( 'cls' )

if __name__ == "__main__":
    atm( "Dan", 1234 )