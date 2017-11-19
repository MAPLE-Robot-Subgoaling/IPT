def main():
    tempt = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == 'C':
        if tempt <= 0: 
            print("At this temperature, water is a (frozen) solid.")
        elif tempt > 0 and tempt < 100:
            print("At this temperature, water is a liquid.")
        elif tempt >= 100:
            print("At this temperature, water is a gas.")
    if scale == 'K':
        if tempt <= 273.16:
            print("At this temperature, water is a (frozen) solid.")
        elif tempt > 273.16 and tempt < 373.16:
            print("At this temperature, water is a liquid.")
        elif tempt >= 373.16:
            print("At this temperature, water is a gas.")
main()
