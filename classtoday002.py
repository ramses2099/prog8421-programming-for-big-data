#!/usr/bin/env python3
from os import system

def add_numbers(num1, num2):
    return (num1 + num2)

def sub_numbers(num1, num2):
    return (num1 - num2)

def div_numbers(num1, num2):
    return (num1 / num2)

def mult_numbers(num1, num2):
    return (num1 * num2)
      
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

def menu():
    system("clear")
    print()
    while True:        
        print("\nMenu:")
        print("1. Add Numbers")
        print("2. Sub Numbers")
        print("3. Mult Numbers")
        print("4. Div Numbers")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            exit_program()
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))            
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        if choice == '1':
            rs = add_numbers(num1, num2)            
            print(f"The sum of {num1} and {num2} is {rs}.")
        elif choice == '2':
            rs = sub_numbers(num1, num2)
            print(f"The sub of {num1} and {num2} is {rs}.")        
        elif choice == '3':
            rs = mult_numbers(num1, num2)
            print(f"The mult of {num1} and {num2} is {rs}.")        
        elif choice == '4':
            rs = div_numbers(num1, num2)
            print(f"The div of {num1} and {num2} is {rs}.")        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()