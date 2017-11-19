def main():
    temp = float(input("Enter the temperature: "))
    unit = str(input("Enter 'C' for Celsius or 'K' for Kelvin: "))
    if unit == "C":
        if temp >= 100:
            print("At this temperature, water is a gas.")
        elif temp > 20:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a (frozen) solid.")
    else:
        if temp >= 373:
            print("At this temperature, water is a gas.")
        elif temp > 273:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a (frozen) solid.")
main()
