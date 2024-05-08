#!/env/bin/ python3

# Miles Per Gallon Program
def main():
    print("The Miles Per Gallon program")
    print("============================")
    miles_driven = float(input("Enter miles driven: \t\t"))
    gallons_used = float(input("Enter gallons of gas used: \t"))
    
    mpg = miles_driven / gallons_used
    mpg = round(mpg, 2)
    
    print()
    print(f"Miles Per Gallon: \t\t{mpg}")
    print()
    print("Bye!")
    
    

if __name__ == "__main__":
    main()