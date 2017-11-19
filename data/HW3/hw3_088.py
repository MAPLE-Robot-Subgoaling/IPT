def main():
    temp = float(input("Enter a temperature: "))
    scale = input("Enter the scale for the temperature 'K' for Kelvin or 'C' for Celsius: "))
    if scale == "C":
        if temp >= 100:
            print("At this temperature, water is a gas.")
        elif temp <= 0:
            print("At this temperature, water is a solid.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if temp <= 273.15:
            print("At this temperature, water is a solid.")
        elif temp >= 373.15:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
main()
