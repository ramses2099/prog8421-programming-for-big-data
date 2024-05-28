#!/env/bin/ python3
import os
import math

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
 
def main():
    os.system("clear")
    your_num = int(input("Enter a number: "))
    while (your_num > 0):
        product = your_num * 5
        print(f"{your_num} * 5 = {product}")
        your_num -= 1
    
    
if __name__ == "__main__":
    main()