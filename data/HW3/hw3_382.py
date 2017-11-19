def main():
    userTemp = float(input("Please enter a temperature:"))
    tempValue = input("Please enter 'C' for Celsius, or 'K' for Kelvin")
    if tempValue == "C":
        if userTemp <= 100:
            print("At this temperature, water is a liquid.")
        elif userTemp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a gas.")
    if tempValue == "K":
        if userTemp <= 373:
            print("At this temperature, water is a liquid.")
        elif userTemp <= 272:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a gas.")
main()
