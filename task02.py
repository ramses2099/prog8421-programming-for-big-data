#!/env/bin/ python3

# constant for interest per year
INTERST_PER_YEAR = 0.04


def main():
    print("============================================")
    print("Welcome to savings account earns for year")
    print("============================================")
    
    choice = "y"
    while choice.lower() == "y":
        a_money = float(input("Enter the total amount of money deposited: \t"))
        # first year of interest
        s_f_year = a_money + (a_money * INTERST_PER_YEAR)
              
        # second year of interest
        s_s_year = s_f_year + (s_f_year * INTERST_PER_YEAR)
        
        # second year of interest
        s_t_year = s_s_year + (s_s_year * INTERST_PER_YEAR)
        
      
        print("------------------------------------------")
        print(f"The amount in the savings account after 1 year:\t{s_f_year:.2f}")
        print(f"The amount in the savings account after 2 year:\t{s_s_year:.2f}")
        print(f"The amount in the savings account after 3 year:\t{s_t_year:.2f}")
        print("------------------------------------------")
        choice = str(input("Continue? (y/n): ")).lower()
        
        print()
    print("Bye!")

if __name__ == "__main__":
    main()