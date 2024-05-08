#!/env/bin/ python3

import locale

def main():
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    print("Welcome to the Future Value Calculator")
    print("=======================================")
    
    choice = "y"
    while choice.lower() == "y":
        m_invest = float(input("Enter monthly investment: \t"))
        y_invest_r = float(input("Enter yearly interest rate: \t"))
        years = int(input("Enter number of years: \t\t"))
        
        m_interest_r = (y_invest_r / 12 / 100)
        months = years * 12
        fut_value = 0
        for i in range(months):
            fut_value += m_invest
            m_interest_amount = fut_value * m_interest_r
            fut_value += m_interest_amount
        print("Fucture value:\t\t\t" + locale.currency(fut_value, grouping=True))
        print()
        
        choice = str(input("Continue? (y/n): ")).lower()
        
        print()
    print("Bye!")

if __name__ == "__main__":
    main()