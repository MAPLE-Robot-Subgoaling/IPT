

def main():
    temp = float(input("Please enter the temperature: "))
    scaleT = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if scaleT == "C":
        if temp < 0:
            print("At this Temperature: (",temp, scaleT,"), water is a (frozen) solid.")
        elif temp >= 0 and temp < 100:
            print("At this temperature: (",temp, scaleT,"), water is a liquid.")
        else:
            print("At this temperature: (",temp, scaleT,"), water is a gas.")

    elif scaleT == "K":
        if temp < 273.2:
            print("At this temperature: (",temp, scaleT,"), water is a (frozen) solid.")
        elif temp >= 273.2 and temp < 373.2:
            print("At this temperature: (",temp, scaleT,"), water is a liquid.")
        else:
            print("At this temperature: (",temp, scaleT,") water is a gas.")

    else:
        print("That is not a recognized temperature scale, sorry.")

    print()

main()
