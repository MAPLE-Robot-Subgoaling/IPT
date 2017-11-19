def main():
    temp = float(input("Enter the temperature:"))
    tempType = input("Enter 'c' for Celsius, or 'k' for Kelvin:")
    if tempType == "c":
        if temp >= 100:
            print("At this temperature, water is a gas.")
        elif temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
    if tempType == "k":
        if temp <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        elif temp >= 373.15:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
main()
