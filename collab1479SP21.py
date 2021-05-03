# Menu program for Programming Final Project
# Used with Github to ensure that students know the GitHub process.

semester = "ITSE1479 - Spring 2021";

def main():
    #*****************************************************************
    # jumpTable for all functions
    # 
    # Modify your line to create a jumpTable entry for your 
    #   function.  Replace stub() with the name of your function that 
    #   you added to the end this code section.
    #
    # Notes:
    #    jumpTables hold the name of a function, not the variables
    #       that are passed to it.  See smileyFunction for a way
    #       to pass variables manually, 
    #       OR create your own inputs inside of your function to 
    #           collect user input.
    #   Use the following code at the end of your function to 
    #       pause the program
    #           print()
    #           print("Press ENTER to return to the menu")
    #           input()
    #   DO NOT TRASH THE CALL TO main() at the end.  Thanks.
    #*****************************************************************
    jumpTable = {}
    jumpTable['1'] = smileyFunction       # Smiley - call to function goes here
    jumpTable['2'] = stub                 # Arcement - call to function goes here
    jumpTable['3'] = stub                 # Burns - call to function goes here
    jumpTable['4'] = stub                 # De Guzman - call to function goes here
    jumpTable['5'] = stub                 # Ezell - call to function goes here
    jumpTable['6'] = stub                 # Goltl - call to function goes here
    jumpTable['7'] = stub                 # Hammad - call to function goes here
    jumpTable['8'] = stub                 # Hopper - call to function goes here
    jumpTable['9'] = stub                 # Newman - call to function goes here
    jumpTable['10'] = stub                # Nguyen - call to function goes here
    jumpTable['11'] = stub                # Rodriguez Rosales - call to function goes here
    jumpTable['12'] = stub                # Seaman - call to function goes here
    jumpTable['13'] = stub                # Silva - call to function goes here
    jumpTable['14'] = stub                # Simmons - call to function goes here
    jumpTable['15'] = stub                # Smith, C - call to function goes here
    jumpTable['16'] = stub                # Smith, J - call to function goes here
    jumpTable['17'] = stub                # Stout - call to function goes here
    jumpTable['18'] = stub                # Syed - call to function goes here
    jumpTable['19'] = stub                # Watts - call to function goes here
    jumpTable['20'] = woolardFunction                # Woolard - call to function goes here

    chrChoice = ""      # To hold a menu choice

    # Constants for the menu choices
    EXIT = '0';

    while chrChoice != '0':
        # Display the menu and get the user's choice.
        showMenu();
        
        chrChoice = input("Enter your selection (0 to exit): ")
        
        if(chrChoice.isdigit() and int(chrChoice) < (len(jumpTable) + 1)):
            # Validate the menu selection.
            if chrChoice == EXIT:
                print()
                print("Thank for using the", semester, "Menu Program. ")
                print("Have a nice day.")
            else:
                jumpTable[chrChoice]()
        else:
            print("Please enter one of the numeric values from the menu.  Thanks")
            print("Press ENTER to continue.")
            input()    

            

#*****************************************************************
# Definition of function showMenu which displays the menu.       *
#*****************************************************************

def showMenu():
    print("*******************************************************************")
    print("*   Welcome to the ", semester, " Program!")
    print("*      Make a selection from the list below to see student output *")
    print("*                                                                 *")
    print("*      Enter 0 and press Enter to Quit.                           *")
    print("*******************************************************************")

    print("1.  Smiley")
    print("2.  Arcement")
    print("3.  Burns")
    print("4.  De Guzman")
    print("5.  Ezell")
    print("6.  Goltl")
    print("7.  Hammad")
    print("8.  Hopper")
    print("9.  Newman")
    print("10. Nguyen")
    print("11. Rodriguez Rosales")
    print("12. Seaman")
    print("13. Silva")
    print("14. Simmons")
    print("15. Smith, C")
    print("16. Smith, J")
    print("17. Stout")
    print("18. Syed")
    print("19. Watts")
    print("20. Woolard")
    print()

# *****************************************************************************************
# Function Definitions Section
# *****************************************************************************************
# Add your function below.  
#  
# FunctionName:  lastnameFunction(your parameters)
# *****************************************************************************************

def woolardFunction():
    woolardGame()
    print("""               _________________________
              |\ _____________________ /|
              | |_____________________| |
              |/_______________________\|
              /=========================\\
             '==========================='
              |  ~~                  ~~ |
              |         R.I.P.          |
              |_________________________|""")
            
    print("Press ENTER to continue.")
    input()
    
    
def woolardGame():
    selection = ["yes", "no", "x"]
    direction = ["forward", "backward", "left", "right"]
    
    print("*" * 80)
    print("Welcome to R. I. P.   A choose your own adventure game. Good luck!")
    print("*" * 80)
    
    #The game begins
    name = input("Please enter your character name: ")
    print("Welcome", name)
    print("-" * 80)
    print(name, "has once again woke up in a dark room with no clue how they "
          "got there or memory of the night before.\n")
    print("Would you like to look around the room?")
    
    choice = ""
    while choice not in selection:
        choice = input("Please type in yes or no, or simply enter x to exit the game: ")
        print("-" * 80)
        if choice == "yes":
            print("You look around the room and realize it is indeed dark.")
            print(name, "is doing great so far, everything will work out fine.")
        elif choice == "no":
            print("Your lack of inquisitiveness has rewarded you with... well nothing.")
        elif choice == "x":
            print("You have chose to sit and do nothing, playing this game is way too hard.")
            print(name, "has died of thirst and general apathy.")
            return
        else:
            print("That input was not recognized, please enter yes, no or x to exit.")
            
    print("-" * 80)
    print("You are still in the dark and confused but you get the sense you can leave the room "
          "by heading in any direction.")
    choice = ""
    while choice not in direction:
        choice = input("Please choose a direction to go, type in left, right, forward or backward or x to exit: ")
        print("-" * 80)
        if choice == "forward":
            print("You start to walk forward, it quickly becomes apparent that you are facing the edge of a cliff!")
            print("Before you can stop yourself you stumble over the edge and vanish into the abyss.")
            print(name, "has fallen to their death.")
        elif choice == "backward":
            print("You don't bother turning around and start walking backwards.")
            print("After taking several steps backwards you sense a presence behind you.")
            print("Thanks to your finely honed reflexes you turn around quickly to see what lurks behind you!")
            print("Due to your lack of night vision and the fact that it's dark you don't see anything.")
            print(name, "was mauled to death by a... shark or a bear or something.")
        elif choice == "left":
            print("You turn and start walking to your left, at least you think it's your left. Directions are hard.")
            print(name, "has died in a mostly leftward direction.")
        elif choice == "right":
            print("You confidently turn to your right and start to walk.")
            print("After walking with a determined step for a several minutes you smack into a wall.")
            print(name, "is adamant about that determined stride and continues to walk into the wall.")
            print(name, "has died because once you make a choice you stick to it, nobody changes your mind.")
        else:
            print("That input was not recognized, please enter yes, no or x to exit.")


# *****************************************************************************************
# FUNCTION:         stub (default for menu)
# DESCRIPTION:      stub function created to print a single message: Not Implemented Yet
# OUTPUT EXAMPLE:   User enters any jumpTable entry that has not been created yet
# *****************************************************************************************
def stub():
    print()
    print()

    print("Not implemented at this time.  Check back later.")
    print("Press ENTER to continue.")
    input()    

# *****************************************************************************************
# FUNCTION:         smileyFunction
# DESCRIPTION:      calls SmileyFib with a parameter of 11
#                   prints the Fibonacci series as defined by the input value
# OUTPUT EXAMPLE:   User enters 11
#                   Program outputs the following:
#                      Fibonacci Sequence (9 iterations): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# *****************************************************************************************
def smileyFunction():
    smileyFib(11)
    print("Press ENTER to continue.")
    input()    

def smileyFib(numberOfTimes):
    current = 0
    nextOne = 1
    nextTerm = 0

    print()
    print()
    print("Fibonacci Sequence (", str(numberOfTimes)," iterations)")

    for i in range(0, numberOfTimes):
        if (i == 1):                    # Prints the first term
            print(str(current), end= '')

        elif (i == 2):                 # Prints the second term
            print(str(nextOne), end = '')
        else:                          # Prints all subsequent terms
            nextTerm = current + nextOne;
            current = nextOne;
            nextOne = nextTerm;

            print(str(nextTerm), end = '')

        if (i + 1) < numberOfTimes:
            print(", ", end = '')

    print()
    print()
    


#*****************************************************************
# Please leave me alone,
#   Sincerely,
#       main()
#*****************************************************************
main()
