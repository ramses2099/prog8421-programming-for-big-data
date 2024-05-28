#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Create a program that displays a welcome message and calculates a player’s batting
# average.
# -----------------------------------------------------------------------------------------


def main():
    os.system("clear")
    
    print()
    print(Style.GREEN + "[---------------------Baseball Team Manager-------------------------]")
    print(Style.GREEN + "[---This program calculates the batting average for a player based--]")
    print(Style.GREEN + "[---on the player's official number of at bats and hits.------------]")
    print(Style.GREEN + "[-------------------------------------------------------------------]")
    print()
    
    numbre_of_bats= 0
    number_of_hits= 0
    
    # Player's name: Pat
    player_name = input(Style.BLUE + "Enter the player name:\t")
        
    while True:
        try:
            # Official number of at bats: 11
            numbre_of_bats = int(input("Enter the offical number of at bats:\t"))
        except ValueError:
            print("Enter a valid integer number")
            continue
        else:
            break
        
    while True:
        try:
           # Number of hits: 4
            number_of_hits = int(input("Enter the number of hits:\t"))   
        except ValueError:
            print("Enter a valid integer number")
            continue
        else:
            break
     
    # Pat's batting average is 0.364
    avg = number_of_hits / numbre_of_bats
   
    print()
    print(Style.YELLOW + "[--------------------------OUTPUT-----------------------------------]")
    print()
    print(f"\t{player_name}'s batting average is : ", end="")
    print("{:.3f}".format(avg))
    print()
    print(Style.YELLOW + "[----------------------------OUTPUT---------------------------------]")
    print()
    
if __name__ == "__main__":
    main()