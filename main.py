import rps
import tictac

import sys

def menu():
    print("""
            ************Welcome to SAS Gaming Hub**************""")
    print()

    choice = input("""
                      A: To play Rock Paper Scissors
                      B: To play Tic Tac Toe
                      Q: To exit the application

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        rps.game()
    elif choice == "B" or choice =="b":
        tictac.game()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A, B or C")
        print("Please try again")
        menu()

  
#the program is initiated, so to speak, here
if __name__ == "__main__":
    menu()
