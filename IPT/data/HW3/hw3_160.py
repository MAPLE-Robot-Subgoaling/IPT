def main():
    temp = float (input("Please enter the temperature:"))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if scale == "C":
        if temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        if temp < 100 and temp > 0:
            print("At this temperature, water is a liquid.")
        if temp >= 100:
            print("At this temperature, water is a gas.")
    else:
        if temp <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        if temp < 373.15 and temp > 273.15:
            print("At this temperature, water is a liquid.")
        if temp >= 373.15:
            print("At this temperature, water is a gas.")
main()
