#!/env/bin/ python3

def main():
    counter = 0
    score_total = 0
    test_score = 0
    
    while test_score != 999:
        test_score = int(input("Enter test score: "))
        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
    average_score = round(score_total / counter)
    
    print("===================================")
    # print("Total Score: " + str(score_total))
    # print("Average Score: " +  str(average_score))
    print("Total Score: " + str(score_total) +
          "\nAverage Score: " +  str(average_score))
    

if __name__ == "__main__":
    main()