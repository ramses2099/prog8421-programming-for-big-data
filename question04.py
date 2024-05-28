#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Question-4. Write a program in python for the following input, process, and output
# -----------------------------------------------------------------------------------------

class TravelTime:
    def __init__(self, ml, mlp_hour) -> None:
        """class Travel Time for stored the information required and process"""
        self._ml = ml
        self._mlp_hour = mlp_hour
    
    def cal_number_hours(self):
        return round((self._ml // self._mlp_hour),2)
    
    def cal_number_minutes(self):
        return round((self.cal_number_hours() * 60),2)
        
    def show_output(self):
        print()
        print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
        print(Style.YELLOW + "[-------------ESTIMATED TRAVEL TIME------------------]")
        print(Style.GREEN + f"\tHours: {self.cal_number_hours()}")
        print(Style.GREEN + f"\tMinutes:  {self.cal_number_minutes()}")
        print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
        print()

def main():
    os.system("clear")
    print(Style.BLUE + "[--------------------QUESTION 4----------------------]")
    print(Style.BLUE + "[--------WELCOME TO TRAVEL TIME CALCUALTOR-----------]")
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    ml = float(input("Enter Miles: "))
    mlperh = float(input("Enter Miles per Hour: "))
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    
    tt = TravelTime(ml, mlperh)
    tt.show_output()
   
    
if __name__ == "__main__":
    main()