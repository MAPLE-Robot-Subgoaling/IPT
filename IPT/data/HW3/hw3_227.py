
def main():
    tempWater = float(input("Please enter the temperature:"))
    tempScale = input("Please enter 'C' for Celcius or 'K' for Kelvin:")
    
    if tempScale == "C":
        if tempWater <= 0:
            print("At this temperature, water is a (frozen) solid")
        if tempWater > 0 and tempWater < 100:
            print("At this temperature, water is a liquid")
        if tempWater >= 100:
            print("At this temperature, water is a gas")
    if tempScale == "K":
        if tempWater <= 273:
            print("At this temperature, water is a (frozen) solid")
        if tempWater > 273 and tempWater < 373:
            print("At this temperature, water is a liquid")
        if tempWater >= 373:
            print("At this temperature, water is a gas")
main()
