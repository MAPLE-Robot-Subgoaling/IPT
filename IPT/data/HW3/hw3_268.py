
def main():
    
    tempNum = float(input("Please enter the temperature: "))
    tempScale = input("Enter 'C' for Celsius and 'K' for Kelvin: ")
    
    if tempScale == "C":
        if tempNum < 0:
            print("Water is frozen at", tempNum, "degrees Celsius")
        elif tempNum >= 0 and tempNum < 100:
            print("Water is in it's liquid state at", tempNum, "degrees Celsius")
        elif tempNum >= 100:
            print("Water will boil and turn into a gas at", tempNum, "degrees Celsius")
            
    if tempScale == "K":
        if tempNum < 273.15:
            print("Water is frozen at", tempNum, "Kelvin")
        elif tempNum >= 273.15 and tempNum < 373.15:
            print("Water is in it's liquid state at", tempNum, "Kelvin")
        elif tempNum >= 373.15:
            print("Water will boil and turn into a gas at", tempNum, "Kelvin")

main()
