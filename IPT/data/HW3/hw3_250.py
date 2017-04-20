
def main():
    temp = float(input("Please enter the temperature:  "))
    unit = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin:  "))
    if unit == "C":
        if temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif temp >= 100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if temp <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        elif temp >= 373.2:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")

main()
