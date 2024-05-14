#!/env/bin/ python3
import os

# constant for the value of 1 foot to inches 12
FOOT_TO_INCHES = 12
# constant for the value of 1 inches to centimeter
INCHES_TO_CENTIMETERS = 2.54

"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system.
Write a program that reads a number of feet from the user, followed by a number of
inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters
"""

def main():
    os.system('clear')
    
    print("===============================================")
    print("Welcome to calculate the number of centimeters")
    print("===============================================")
    
    choice = "y"
    while choice.lower() == "y":
        
        # read the input from user
        n_feet = float(input("Enter the number of feet: "))
        
        # read the input from user
        n_inches = float(input("Enter the number of the inches: "))
      
        # convert feet to centimeters6
        f_to_centimeters = (n_feet * FOOT_TO_INCHES) * INCHES_TO_CENTIMETERS
        
        # convert inches to centimeters
        i_to_centimeter = n_inches * INCHES_TO_CENTIMETERS 
        
        total_centemeters = (f_to_centimeters + i_to_centimeter) 

        print("----------------------------------------------")
        print(f"Total centimeters:\t{total_centemeters:.2f}")
        print("----------------------------------------------")
        choice = str(input("Continue? (y/n): ")).lower()
        
        print()
    print("Bye!")

if __name__ == "__main__":
    main()