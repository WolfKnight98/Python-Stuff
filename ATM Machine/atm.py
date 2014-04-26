# Atm

import random, time

class atm:

    def __init__( self, name, pincode ):
        self.name = name
        self.pincode = pincode
        user_name, user_pincode = "", None

        user_name = str( input( "Type your name: " ) )

        if user_name != self.name:
            print( "Invalid name." )
            user_name = False
        elif user_name == self.name:
            print( "Valid name." )
            user_name = True

        try:
            user_pincode = int( input( "Type your pincode: " ) )
        except ValueError:
            print( "Error." )
            exit()

        if user_pincode != self.pincode:
            print( "Invalid pincode." )
            user_pincode = False
        elif user_pincode == self.pincode:
            print( "Valid pincode." )
            user_pincode = True

        if user_name and user_pincode == True:
            print( "Valid user and pincode, booting system." )
            self.main_menu( 0, 1000, 500 )
        else: 
            print( "Invalid user and pincode." )

    def main_menu( self, balance, max_withdraw, max_deposit ):
        self.balance = balance
        self.max_withdraw = max_withdraw
        self.max_deposit = max_deposit