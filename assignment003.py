#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Question-3. Enhance the Miles Per Gallon program that we discussed in class, so the console display looks something
# like this:
# The Miles Per Gallon program
# Enter miles driven: 150
# Enter gallons of gas used: 15.2
# Enter cost per gallon: 4.25
# Miles Per Gallon: 9.87
# Total Gas Cost: 64.6
# Cost Per Mile: 0.4
# Get entries for another trip (y/n)? y
# -----------------------------------------------------------------------------------------

# function for validate the input number
def is_valid_number(input_str):
    try:
        val = float(input_str)
        if val > 0:
            return True
        else:
            print("Please enter a positive number.")
            return False
    except ValueError:
        print("Please enter a valid number.")
        return False
    
# function for validate the input number
def get_positive_number(prompt):
    while True:
        value = input(prompt)
        if is_valid_number(value):
            return float(value)

def main():
    os.system("clear")
    print(Style.BLUE + "[--------------------QUESTION 3----------------------]")
    print(Style.BLUE + "[------------THE MILES PER GALLON PROGRAM------------]")
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    
    # declare variable
    miles_driven = 0
    gallons_used = 0
    cost_per_gallon = 0
    
    while True:
        print("")
        miles_driven = get_positive_number(Style.BLUE + "Enter miles driven: ")
        gallons_used = get_positive_number(Style.BLUE + "Enter gallons of gas used: ")
        cost_per_gallon = get_positive_number(Style.BLUE + "Enter cost per gallon: ")

        miles_per_gallon = miles_driven / gallons_used
        total_gas_cost = gallons_used * cost_per_gallon
        cost_per_mile = total_gas_cost / miles_driven

        print()
        print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
        print(Style.YELLOW +f"Miles Per Gallon: {miles_per_gallon:.2f}")
        print(Style.YELLOW +f"Total Gas Cost: {total_gas_cost:.2f}")
        print(Style.YELLOW +f"Cost Per Mile: {cost_per_mile:.2f}")
        print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
        print()

        another_trip = input("Get entries for another trip (y/n)? ").lower()
        if another_trip != 'y':
            break
        
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
        
    
if __name__ == "__main__":
    main()