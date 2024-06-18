#!/env/bin/ python3
import os


# -----------------------------------------------------------------------------------------
# Pruduct inventory using list
# -----------------------------------------------------------------------------------------

# Class of different styles
class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

class Product:
    """
    Class Product
    """
    def __init__(self, ids, name, price):
      self._id = ids
      self._name = name
      self._price = price
      
    def toString(self):
        return f"id: {self._id}, product name: {self._name}, price: {round(self._price,2)}"
      
class Inventory:
    """
    Class inventory
    """
    def __init__(self):
      self._data = list()
    
    def add_product(self, item: Product):
        """method add product to the list"""
        self._data.append(item)
        
    def delete_product(self, ids):
        """method remove element to the list"""
        if ids < 0 or ids > len(self._data):
            raise ValueError("No product id")
        else:
            return self._data.pop(ids-1)
        
    def list_product(self):
        """method list all element of the list"""
        if self.list_size() > 0:
            return self._data
        else:
            raise IndexError("No eleement in the list")
    @staticmethod
    def sorted_list(inv, desc):
        if desc:           
            return sorted(inv._data, key=lambda i: i._id, reverse=True) 
        else:
            return inv._data
            
    
    def list_size(self):
        return len(self._data)

def display_menu():
    print(Style.GREEN + "COMMAND MENU")
    print(Style.GREEN +"list - List all Product")
    print(Style.GREEN +"add - Add a Product")
    print(Style.GREEN +"del - Delete a Product")
    print(Style.GREEN +"sort - Delete a Product")
    print(Style.GREEN +"exit - Exit program")
    print()

# GLOBAL VAR
inv = Inventory()

def listar():    
    print()
    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    for i, p in enumerate(inv.list_product(), start=1):
        print(f"\t{i}. {p.toString()}")    
    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    print()

def add():
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    ids = int(input(Style.BLUE + "\tEnter id product: "))
    name = input(Style.BLUE + "\tEnter name product: ")
    price = float(input(Style.BLUE +"\tEnter prices product: "))
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    inv.add_product(Product(ids, name, price))

def delete():
    print(Style.BLUE + "[---------------------OUTPUT--------------------------]")
    ids = int(input(Style.BLUE + "\tEnter id product for delete: "))
    p = inv.delete_product(ids)
    print(Style.RED + f"Product delete {p.toString()}")
    print(Style.BLUE + "[---------------------OUTPUT--------------------------]")

def sorteds():
    print()
    print(Style.YELLOW + "[---------------------SORTED LIST-------------------------]")
    l = int(input(Style.BLUE + "\tEnter 0 - for sort desc or 1 - for sort asc: "))
    t = False
    if l == 1:
        t = True
           
    for i, p in enumerate(Inventory.sorted_list(inv,t)):
        print(f"\t{i}. {p.toString()}")    
    print(Style.YELLOW + "[---------------------SORTED LIST-------------------------]")
    print()

def main():
    os.system("clear")
    print(Style.BLUE + "[----------------------------------------------------]")
    print(Style.BLUE + "[------------------PRODUCT INVENTORY-----------------]")
    
        
    inv.add_product(Product(1, "Apple", 37.0))
    inv.add_product(Product(2, "Orange", 7.0))
    inv.add_product(Product(3, "Banana", 10.0))
    
    # display menu
    display_menu()    
    
    while True:
        print("")  
        command = input("Command: ")
        if command.lower() == "list":
            listar()
        elif command.lower() == "add":
            add()
        elif command.lower() == "del":
            delete()
        elif command.lower() == "sort":
            sorteds()
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")     
    
    
if __name__ == "__main__":
    main()