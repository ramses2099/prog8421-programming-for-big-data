#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Question-3. Write a program in Python to perform the following tasks.
# -----------------------------------------------------------------------------------------

class TipCalculator:
    def __init__(self, cfm, tp) -> None:
        """class Tip Calculator for stored the information required and process"""
        self._c_ofm = cfm
        self._t_per = tp
    
    def cal_tip_amount(self):
        return round((self._c_ofm * self._t_per),2)
    
    def cal_total_amount(self):
        return round((self._c_ofm + self.cal_tip_amount()),2)
        
    def show_output(self):
        print()
        print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
        print(Style.GREEN + f"\tTip amount: {self.cal_tip_amount()}")
        print(Style.GREEN + f"\tTotal amount:  {self.cal_total_amount()}")
        print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
        print()

def main():
    os.system("clear")
    print(Style.BLUE + "[--------------------QUESTION 3----------------------]")
    print(Style.BLUE + "[--------------WELCOME TO TIP CALCULATOR-------------]")
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    cfm = float(input("Enter Cost of Meal: "))
    tp = float(input("Enter Tip percent: "))
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    
    tc = TipCalculator(cfm, tp)
    tc.show_output()
   
    
if __name__ == "__main__":
    main()