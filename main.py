#!/env/bin/ python3
import os
import math
from temperature import temperature

def discount_percent(invoice_t, cust_type):
    disc_per = 0
    msg = "discount % is"
    cust_type = cust_type.lower()
    if(cust_type == "r"):
        if(invoice_t < 100):
            msg += str(disc_per)
        elif(invoice_t >= 100 and invoice_t < 250):
            disc_per = 1
            msg += str(disc_per)
        elif(invoice_t >= 250):
            disc_per = 2
            msg += str(disc_per)
    elif(cust_type == "w"):
        if(invoice_t < 500):
            disc_per = 4
            msg += str(disc_per)
        elif(invoice_t >= 500):
            disc_per = 5
            msg += str(disc_per)
       
    else:
        msg += 0
        print(msg)
        return
    print(msg)
 

to_celsius = lambda fahrenheit: (fahrenheit - 32) * 5/9 
 
 
def main():
    os.system("clear")
    
    t = temperature.to_celsius(25)
    print(t)
    
    # Map with lambda
    # A Python lambda makes the map function far more concise.
    myList = [10, 25, 17, 9, 30, -5]
    # Double the value of each element
    myList2 = map(lambda n : n*2, myList)
    
    for v in myList2:
        print(v)
    
    rs = to_celsius(25)
    print(rs)
    
    # Filter with lambda
    # Lambdas can also simplify the filter() function.
    # Filters the elements which are not multiples of 5
    myList3 = filter(lambda n : n%5 == 0, myList)
    for v in myList3:
        print(v)
    
    
    
    
if __name__ == "__main__":
    main()