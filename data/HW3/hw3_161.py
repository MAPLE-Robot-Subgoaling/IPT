def main():
    temperature = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        if 0 < temperature < 100: 
            print("At this temperature, water is a liquid.")
        elif 0 > temperature:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a gas.")
    else:
        if 273.15 < temperature < 373.15:
            print("At this temperature, water is a liquid.")
        elif 273.15 > temperature:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a gas.")
main()
