#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Write an algorithm/flowchart and a Python program to find those numbers
# which are divisible by 4 and multiples of 5, between 10 and 100 (both included)
# Hints:
# • Iterate through (Loop) numbers from 10 to 100 (inclusive)
# • Check if the number is divisible by 4 and 5 without any remainder.
# -----------------------------------------------------------------------------------------


def main():
    os.system("clear")
    rsv4, rsv5 = "","";
    
    for i in range(10,100):
        if i % 4 == 0:
            rsv4 += str(i) +","
        if i % 5 == 0:
            rsv5 += str(i) +","
   
    print()
    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    print()
    print(Style.GREEN + f"Number is divisible by 4 = {rsv4}")
    print(Style.BLUE + f"Number is divisible by 5 = {rsv5}")
    print()
    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    print()
    
if __name__ == "__main__":
    main()