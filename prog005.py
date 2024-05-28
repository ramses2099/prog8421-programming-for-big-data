#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Write a Python program to construct the following pattern, using a nested for loop.
# -----------------------------------------------------------------------------------------

def print_start(i):
    sr = ""
    for l in range(i):
        sr += "* "
    return sr


def main():
    os.system("clear")
     
    for i in range(1,6):
        print(print_start(i))
        if i >= 5:
            for l in range(i, 0, -1):
                 print(print_start(l))
        
if __name__ == "__main__":
    main()
	

