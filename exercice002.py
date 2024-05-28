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
    
    print(Style.GREEN + "[--------------------------MENU OPTIONS-----------------------------]")
    print(Style.GREEN + "[----------------------- 1 - Calculate batting average--------------]")
    print(Style.GREEN + "[----------------------- 2 - Exit program---------------------------]")
    print(Style.GREEN + "[-------------------------------------------------------------------]")
   
    option = 0
    numbre_of_bats= 0
    number_of_hits= 0
    
    while True:
        try:
            print()
            # Official number of at bats: 11
            option = int(input("\tEnter the option:\t"))
            if option < 1 or option > 2:
                print("Enter a valid integer number")
                continue
            
            if option == 1:
                print()
                print(Style.BLUE + "[-------------------------- Menu Option 1---------------------------]")
                print(Style.BLUE + "[-------------------Calculate batting average...--------------------]")
                print()
                
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
                
            elif option == 2:
                print()
                print("Bye!")
                break
            
        except ValueError:
            print("Enter a valid integer number")
            continue
        else:
            break
    
     
   
   
   
    
if __name__ == "__main__":
    main()