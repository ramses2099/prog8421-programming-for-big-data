#!/env/bin/ python3
import os
import math
from temperature import temperature
 
 
def main():
    os.system("clear")
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(temperature.to_celsius(temp)), "Celsius")
    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(temperature.to_fahrenheit(temp)), "Fahrenheit")
    
if __name__ == "__main__":
    main()