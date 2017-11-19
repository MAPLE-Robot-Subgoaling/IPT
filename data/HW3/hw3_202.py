tempOfWater = float(input("please enter the temperature: "))
tempType = input("please enter 'C' for celcius, or 'K' for Kelvin: ")
if tempType == "C":
    if tempOfWater <= 0:
        print("at this temperature, water is a solid. ")
    elif tempOfWater > 0 and tempOfWater <= 99:
        print("at this temperature, water is a liquid. ")
    elif tempOfWater >= 100:
        print("at this temperature, water is a gas. ")
elif tempType == "K":
    newTempOfWater = tempOfWater - 273.15
    if newTempOfWater <= 0:
        print("at this temperature, water is a solid. ")
    elif newTempOfWater > 0 and newTempOfWater <= 99:
        print("at this temperature, water is a liquid. ")
    elif newTempOfWater >= 100:
        print("at this temperature, water is a gas. ")
