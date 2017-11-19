def main():
    myTemp = float(input("Please enter the temperature: "))
    myDegrees = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if myDegrees == "C":
        if myTemp <= 0.0:
            print("At this temperature, water is a (frozen) solid.")
        elif 0.0 < myTemp < 100.0:
            print("At this temperature, water is a liquid.")
        elif myTemp >= 100.0:
            print("At this temperature, water is a gas.")
    elif myDegrees == "K":
        if myTemp < 273.16:
            print("At this temperature, water is a (frozen) solid.")
        elif 273.16 <= myTemp < 373.16:
            print("At this temperature, water is a liquid.")
        elif myTemp >= 373.16:
            print("At this temperature, water is a gas.")
main()
