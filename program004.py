#!/env/bin/ python3

def main():
    print("The Test Socres program")
    print()
    print("Enter 3 test scores")
    print("========================")
    
    total_score = 0
    for i in range(3):
        total_score += int(input("Enter test score: "))
    
    average_score = round(total_score / 3)
    print("=========================")
    print("Total Score: ", total_score, 
          "\nAverage Score:", average_score)
    print()
    print("Bye!")

if __name__ == "__main__":
    main()