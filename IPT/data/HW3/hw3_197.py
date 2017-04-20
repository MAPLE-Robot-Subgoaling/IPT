
def main():

    tempNum = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if tempScale == "C":
        if tempNum >= 100:
            print("At this temperature, water is a gas.")
        elif tempNum <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif tempNum > 0 and tempNum < 100:
            print("At this temperature, water is a liquid.")
    if tempScale == "K":
        if tempNum <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        elif tempNum >= 373.15:
            print("At this temperature, water is a gas.")
        elif tempNum > 273.15 and tempNum < 373.15:
            print("At this temperature, water is a liquid.")



main()
