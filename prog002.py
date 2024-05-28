#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Write a Python program to construct the following pattern, using a nested for loop.
# -----------------------------------------------------------------------------------------



def main():
    os.system("clear")
    patter = [[None,None,None,None,'*'],
              [None,None,None,'*','*'],
              [None,None,'*','*','*'],
              [None,'*','*','*','*'],
              ['*','*','*','*','*'],
              [None,'*','*','*','*'],
              [None,None,'*','*','*'],
              [None,None,None,'*','*'],
              [None,None,None,None,'*']]
    
    start =""
    
    for i in range(len(patter)):
       for l in range(len(patter[i])):
           start += "\t"
           if patter[i][l] != None:
               start += "*"
       start += "\n"
    print(Style.GREEN + start)

if __name__ == "__main__":
    main()