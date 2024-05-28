#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Question-1. Write a Python Program that asks you your name (first and last), birth year
# and display the output shown in the following sample output.
# -----------------------------------------------------------------------------------------

class Person:
    def __init__(self, firstname, lastname, year) -> None:
        """class person for stored the information required"""
        self._firstname = firstname
        self._lastname = lastname
        self._year = year
    
    def print_fullname(self):
        return f"{self._firstname} {self._lastname}"
    
    def print_password(self):
        return f"{self._firstname}*{self._year}"
    
    def show_person(self):
        print()
        print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
        print(Style.GREEN + f"\tWelcome {self.print_fullname()}")
        print(Style.GREEN + "\tYour registration is complete.")
        print(Style.GREEN + f"\tYour temporary password is: {self.print_password()} ")
        print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
        print()

def main():
    os.system("clear")
    print(Style.BLUE + "[--------------------QUESTION 1----------------------]")
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    p_firstname = input("First name: ")
    p_lastname = input("Last name: ")
    p_year = int(input("Birth Year: "))
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    p = Person(p_firstname, p_lastname, p_year)
    p.show_person()
    
    
if __name__ == "__main__":
    main()