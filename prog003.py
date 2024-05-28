#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Write a Python program that accepts a word from the user and reverses it.
# -----------------------------------------------------------------------------------------


def main():
    os.system("clear")
    word = input("Enter a word: \t\t")
    rev_word = "";
    l = len(word) -1    
    
    while(l >=0 ):
        rev_word += word[l]
        l -= 1
                 
    print()
    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    print()
    # print(Style.GREEN + f"The word in reverses {word[::-1]}")
    print(Style.GREEN + f"The word in reverses {rev_word}")
    print()
    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    print()
    
if __name__ == "__main__":
    main()