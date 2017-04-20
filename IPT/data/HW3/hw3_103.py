
def main():
    tempUnit  = str(input("Which unit are we using? Use  'C' for Celsius and 'K' for Kelvin"))
    
    if tempUnit == "C":
        tempNum = float(input("What temperature is the water?"))
        if tempNum <= 0:
            print("Your water is frozen solid!")
        if tempNum >= 100:
            print("Your water is gaseous!")
        if tempNum < 100 and tempNum > 0:
            print("Your water is a liquid!")
    if tempUnit == "K":
        tempNum = float(input("What temperature is the water?"))
        if tempNum <= 273.16:
            print("Your water is frozen solid!")
        if tempNum >= 373.16:
            print("Your water is a gas!")
        if tempNum < 373.16 and tempNum > 273.16:
            print("Your water is a liquid!")
main()
