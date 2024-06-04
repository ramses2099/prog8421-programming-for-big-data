#!/env/bin/ python3
import os
from style import Style
import random

LIMIT = 10


def display_title():
    print("Guess the number!\n")


def play_game():
    number = random.randint(1, LIMIT)
    print(f"I'm thinking of a number from 1 to {LIMIT}\n")
    count = 1
    while (guess := int(input("Your guess: "))) != number:
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
    print(f"You guessed it in {count} tries.\n")


def main():
    os.system("clear")
    display_title()
    again = "y"
    while again.lower() == "y":
        play_game()
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")
              
    
    
if __name__ == "__main__":
    main()