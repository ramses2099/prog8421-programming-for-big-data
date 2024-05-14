#!/env/bin/ python3
import os
from style import Style

def main():
    os.system('clear')
    print("===============================")
    print("The Test Socres program")
    print()
    print("Enter 3 test scores")
    print("===============================")
    
    total_score = 0
    for i in range(3):
        total_score += int(input("Enter test score: "))
    
    average_score = round(total_score / 3)
    print("===============================")
    print(Style.GREEN + "Total Score: ", total_score, 
          "\nAverage Score:", average_score)
    print()
    print(Style.WHITE + "Bye!")

if __name__ == "__main__":
    main()