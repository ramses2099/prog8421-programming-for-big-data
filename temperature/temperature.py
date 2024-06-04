"""
This module contains functions for converting
between degrees Fahrenheit and degrees Celsius
"""
def to_celsius(fahrenheit):
    """
    Accepts degrees Fahrenheit (fahrenheit argument)
    Returns degrees Celsius
    """
    return (fahrenheit - 32) * 5/9 
 
def to_fahrenheit(celsius):
    """
    Accepts degrees Celsius (celsius argument)
    Returns degrees Fahrenheit
    """
    return (celsius * 9/5) + 32