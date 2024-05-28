#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Write a Python program that iterates the integers from 1 to 50. For multiples of
# three print "M3" instead of the number and for multiples of five print "M5". For
# numbers that are multiples of three and five, print "M3M5"
# -----------------------------------------------------------------------------------------


def main():
    os.system("clear")
    rsv3, rsv5, rsv35 = "","",""
    
    for i in range(1,50):
        if i % 3 == 0:
            rsv3 += str(i) +"- M3,"
        if i % 5 == 0:
            rsv5 += str(i) +"- M5,"
        if i % 3== 0 and i % 5 == 0:
            rsv35 += str(i) +"- M3 and M5,"
   
    print()
    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    print()
    print(Style.GREEN + f"Number is divisible by 3 = {rsv3}")
    print(Style.BLUE + f"Number is divisible by 5 = {rsv5}")
    print(Style.RED + f"Number is divisible by 3 and 5 = {rsv35}")
    print()
    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    print()
    
if __name__ == "__main__":
    main()