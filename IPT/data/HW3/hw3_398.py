
def main():
    
    freezingPointC = 0
    boilingPointC = 100
    
    freezingPointK = 273.15
    boilingPointK = 373.15

    tempValue = float(input("Please enter the temperature: "))
    scaleType = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    
    if scaleType == 'C':
        if tempValue <= freezingPointC:
            print("At this temperature, water is a (frozen) solid.")
        elif tempValue > freezingPointC and tempValue < boilingPointC:
            print("At this temperature, water is a liquid.")
        elif tempValue > boilingPointC:
            print("At this temperature, water is a gas.")
    elif scaleType == 'K':
        if tempValue <= freezingPointK:
            print("At this temperature, water is a (frozen) solid.")
        elif tempValue > freezingPointK and tempValue < boilingPointK:
            print("At this temperature, water is a liquid.")
        elif tempValue > boilingPointK:
            print("At this temperature, water is a gas.")

main()
