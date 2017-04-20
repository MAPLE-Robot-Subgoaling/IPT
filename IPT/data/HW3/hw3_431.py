''' File: hw3_part3.py 
    Author: Skye Ortiz 
    Date: 09/27/2016 
    Section: 26 
    E-mail: sortiz1@umbc.edu 
    Description: This program tells the user what the state of
    water is at a certain temperature on the temperature scale.
    Collaboration: I did not collaborate with anyone on this assignment.
'''
def main():
    temperature = float(input("Please enter the temperature"))
    degrees = input("Please enter \"C\" for Celcius or \"K\" for Kelvin.")

    if degrees == "C":
        if temperature <= 0:
            print("Water is a solid at that temperature.")
        elif temperature >= 100:
            print("Water is a gas at that temperature.")
        else:
            print("Water is liquid at that temperature.")
    else:
        if temperature <= 273.2:
            print("Water is a solid at that temperature.")
        elif temperature >= 373.2:
            print("Water is a gas at that temperature.")
        else:
            print("Water is liquid at that temperature.")

main() 
