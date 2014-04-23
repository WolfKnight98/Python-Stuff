#Hangman v2 by Dan Hook
import random, os

# If you're playing this game with python shell (IDLE) then leave
# the os.system( 'cls' ) 's commented, if you're using
# the console then uncomment them for nicer use

words_list = [ "Apple", "Batman", "Device", "Steam", "Hashtag", "Map", "Snake", "Letter", "Quater", "Jaguar", "Health", "Desperate",
                       "Confused", "Wonderful", "Confusion", "danisthebest" ]

class hangman:
    def game_intro( self ):
        print( "Welcome to Dan's second hangman game, because the first one screwed up." )
        print( "Are you ready to play? \nType 'Yes' or 'No' " )
        game_start = str( input( " >>>  " ) ).lower()

        if game_start == "yes":
            print( "Let the game begin.." )
            self.game_start()
        elif game_start == "no":
            print( "Well fine then!" )
            exit()
        else:
            print( "I said type YES OR NO!" )
            self.game_intro()
        #os.system( 'cls' )


    def game_start( self ):
        print( "I assume you know what Hangman is, if you don't, please leave the rock you live under." )
        print( "The game shall start.\n" )
        #os.system( 'cls' )
        self.core_game()


    def core_game( self ):
        guesses = 0
        allowed_guesses = 10
        letters_used = []
        word = random.choice( words_list ).lower()
        guessed_word = []
        for x in range( len( word ) ):
            guessed_word.append( "_ " )
            
        #print( word )
        
        while ( guesses < 10 ):
            print( "You've got: %s" % ( "".join( guessed_word ) ) )
            print( "You've used: %s" % ( "".join( letters_used ) ) )
            print( "You have %s guesses left\n" % ( allowed_guesses - guesses ) )
            
            u_guess = input( "Guess a letter: " ).lower()
            
            if u_guess in word and not u_guess in letters_used:
                print( "You got a letter!\n" )
                letters_used.append( u_guess )
                guessed_word = "".join( [ char if char in letters_used else "_ " for char in word ] )
            elif not u_guess in word:
                print( "You didn't get a letter.\n" )
                guesses = guesses + 1
                if u_guess in letters_used:
                    print( "You've already used that letter." )
                else:
                    letters_used.append( u_guess )

            if guessed_word == word:
                print( "You win the game!" )
                print( "The word was: %s" % guessed_word )
                break
            ##os.system( 'cls' )
                
        if guesses == allowed_guesses:
            print( "You lose!" )

        restart_game = input( "Would you like to play again? ( 'Yes' or 'No' ) >>>  " ).lower()
        if restart_game == "yes":
            hangman().core_game()
        elif restart_game == "no":
            exit()
        else:
            print("You didn't type yes or no.")
            

# ----------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    hangman().game_intro()
