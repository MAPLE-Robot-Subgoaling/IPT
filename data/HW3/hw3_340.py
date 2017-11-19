def main():
    temp = float(input("Please enter the temperature: "))
    unit = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if unit == 'C':
        if temp < 0:
            print("At this temperature, water is a (frozen) solid.")
        elif temp > 100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    elif unit == 'K':
        if temp < 273.2:
            print("At this temperature, water is a (frozen) solid.")
        elif temp > 373.2:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        print("Please enter 'C' or 'K'.")
main()
