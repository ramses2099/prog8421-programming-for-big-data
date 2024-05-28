#!/env/bin/ python3
import os
from style import Style

# Miles Per Gallon Program
def main():
    os.system('clear')    
    print("=====================================================")
    print("The Miles Per Gallon program")
    print("=====================================================")
    miles_driven = float(input("Enter miles driven: \t\t"))
    gallons_used = float(input("Enter gallons of gas used: \t"))
    
    if (miles_driven > 0 and gallons_used > 0):
        mpg = miles_driven / gallons_used
        mpg = round(mpg, 2)
        
        print()
        print("-----------------------------------------------------")
        print(Style.GREEN +  f"Miles Per Gallon: \t\t{mpg}")
        print(Style.WHITE + "-----------------------------------------------------")
        print()
        print("Bye!")
    else:
        print("Miles and Gallon must be greater than zero. Try again")

    

if __name__ == "__main__":
    main()