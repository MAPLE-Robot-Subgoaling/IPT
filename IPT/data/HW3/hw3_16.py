def main():
    tempNumber = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempNumber >= 100 and tempScale == 'C':
        print("At this temperature, Water is a gas")
    elif tempNumber < 100 and tempNumber > 0 and tempScale == 'C':
        print("At this temperature, Water is a liquid")
    elif tempNumber <= 0 and tempScale == 'C':
        print("At this temperature, Water is a (frozen) solid")
    elif tempNumber >= 373 and tempScale == 'K':
        print("At this temperature, Water is a gas")
    elif tempNumber < 373 and tempNumber > 273 and tempScale == 'K':
        print("At this temperature, Water is a liquid")
    elif tempNumber <= 273 and tempScale == 'K':
        print("At this temperature, Water is a (frozen) solid")
    
main()
