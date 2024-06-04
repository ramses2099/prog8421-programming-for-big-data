#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Question-1. The length of a month varies from 28 to 31 days. In this exercise you will create a program that reads
# the name of a month from the user as a string. Then your program should display the number of days in that month.
# Display “28 or 29 days” for February so that leap years are addressed.
# -----------------------------------------------------------------------------------------

# Define a dictionary with the number of days in each month
month_days = {
    "January": 31,
    "February": "28 or 29 days",
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

def main():
    os.system("clear")
    print(Style.BLUE + "[--------------------QUESTION 1----------------------]")
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
     # Read the name of the month from the user
    month = input("Enter the name of a month: ")
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
  
    # Convert the month to title case to handle case insensitivity
    month = month.title()
        
    print()
    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    # Display the number of days in the month
    if month in month_days:
        print(Style.GREEN + f"The number of days in {month} is {month_days[month]}.")
    else:
        print(Style.GREEN + "Invalid month name. Please enter a valid month name.")

    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    print()   
    
if __name__ == "__main__":
    main()