def main():
    tempNum = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempScale == "C":
        if tempNum <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif tempNum > 0 and tempNum < 99.99:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    else:
        if tempNum <= 273.16:
            print("At this temperature, water is a (frozen) solid.")
        elif tempNum > 273.16 and tempNum < 373.16:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
main()
