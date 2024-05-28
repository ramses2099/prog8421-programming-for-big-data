#!/env/bin/ python3

# Invoice Program
from style import Style
import os

def main():
    os.system("clear")
    print("==============================================")
    print("The Invoice program")
    print("==============================================")

    cust_type = input("Enter customer type (r/w): \t")
    invoice_total = float(input("Enter invoice total:\t\t"))
    print()
    disc_percent = 0
    if cust_type.lower() == "r":
        if invoice_total > 0 and invoice_total < 100:
            disc_percent = 0
        elif invoice_total >= 100 and invoice_total < 250:
            disc_percent = 0.1
        elif invoice_total >= 250 and invoice_total < 500:
            disc_percent = 0.2
        elif invoice_total >= 500:
            disc_percent = 0.25
    elif cust_type.lower() == "w":
        if invoice_total > 0 and invoice_total <= 100:
            disc_percent = 0.4
        elif invoice_total >= 500:
            disc_percent = 0.5
    else:
        disc_percent = 0

    disc_amount = round(invoice_total * disc_percent, 2)
    new_inv_total = invoice_total - disc_amount

    print(Style.GREEN + f"Invoice total:\t\t\t{invoice_total}")
    print(Style.GREEN + f"Discount percent:\t\t{disc_percent}")
    print(Style.GREEN + f"Discount amount:\t\t{disc_amount}")
    print(Style.GREEN + f"New Invoice total:\t\t{new_inv_total}")
    print(Style.WHITE +"==============================================")
    print()
    print("Bye!")


if __name__ == "__main__":
    main()
