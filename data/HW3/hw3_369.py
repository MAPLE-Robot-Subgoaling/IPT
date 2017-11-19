def main():
    tempDeg=float(input("Please enter the temperature:"))
    tempTyp=str(input("Please enter 'C' for Celsius, or 'K' for Kelvin:"))
    if tempTyp == 'C':
        if tempDeg <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif tempDeg > 0 and tempDeg < 100:
            print("At this temperature, water is a liquid")
        elif tempDeg >= 100:
            print("At this temperature, water is a gas")
    elif tempTyp == 'K':
        if tempDeg <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        elif tempDeg > 273.15 and tempDeg < 373.15:
            print("At this temperature, water is a liquid")
        elif tempDeg >= 373.15:    
            print("At this temperature, water is a gas")
main()
