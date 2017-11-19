def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        if temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif temp < 100:
            print("At this temperature, water is a liquid.")
        elif temp >= 100:
            print("At this temperature, water is a gas.")
    elif scale == "K":
        if temp <= 273.2:
            print("At this temperature, water is a (frozen) solid.")
        elif temp < 373.2:
            print("At this temperature, water is a liquid.")
        elif temp >= 373.2:
            print("At this temperature, water is a gas.")
    else:
        print("You did not enter 'C' or 'K' for the scale.")
main()
