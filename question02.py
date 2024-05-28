#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Question-2. Write a program to perform the following tasks (input, process and output)
# -----------------------------------------------------------------------------------------

class Task:
    def __init__(self, hw, hpr) -> None:
        """class Task for stored the information required and process"""
        self._h_work = hw
        self._h_pay_rate = hpr
        self._tax_r = 18
    
    def cal_tax_amount(self):
        g_pay = self.cal_gross_pay()
        return round((g_pay *(self._tax_r/100)),2)
    
    def cal_gross_pay(self):
        return round((self._h_work * self._h_pay_rate),2)
    
    def take_home_pay(self):
        return round((self.cal_gross_pay()-self.cal_tax_amount()),2)
    
    def show_output(self):
        print()
        print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
        print(Style.GREEN + f"\tGross Pay: {self.cal_gross_pay()}")
        print(Style.GREEN + f"\tTax Rate:  {self._tax_r}%")
        print(Style.GREEN + f"\tTax Amount: {self.cal_tax_amount()} ")
        print(Style.GREEN + f"\tTake Home Pay: {self.take_home_pay()} ")
        print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
        print()

def main():
    os.system("clear")
    print(Style.BLUE + "[--------------------QUESTION 2----------------------]")
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    hw = float(input("Enter Hours Worked: "))
    hpr = float(input("Enter Hours Pay Rate: "))
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    
    t = Task(hw, hpr)
    t.show_output()
   
    
if __name__ == "__main__":
    main()