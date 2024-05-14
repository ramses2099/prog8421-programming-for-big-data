#!/env/bin/ python3
import os

"""
Consider the software that runs on a self-checkout machine. One task that it must be able
to perform is to determine how much change to provide when the shopper pays for a
purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the coins
that should be used to give that amount of change to the shopper. The change should be
given using as few coins as possible. Assume that the machine is loaded with pennies,
nickels, dimes, quarters, loonies and toonies.
"""

def main():
    os.system("clear")

    print("==============================================")
    print("Welcome to calculate the number of cents")
    print("==============================================")
        
        
    choice = "y"
    while choice.lower() == "y":

        # read the input from user
        n_cents = int(input("Enter the number of cents: "))
        msg = "The denominations of the coin is"
        
        if (n_cents == 200):
            msg += " toonies "
        elif(n_cents == 100):
            msg += " loonies "
        elif(n_cents == 25):
            msg += " quarters "
        elif(n_cents == 10): 
            msg += " dimes "
        elif(n_cents == 5):
            msg += " nickels "
        else:
            msg += " pennies "
      
        print("----------------------------------------------")
        print(msg)
        print("----------------------------------------------")
        choice = str(input("Continue? (y/n): ")).lower()

        print()
    print("Bye!")


if __name__ == "__main__":
    main()
