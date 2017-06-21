def main():
    temperature = float(input("Please enter the temperature: "))
    units = str(input("Please enter 'C' for Celcius, or 'K' for Kelvin: "))
    if units == "C":
        if temperature <= 0:
            print("At this temperature, water is a solid")
        elif temperature > 0 and temperature < 100:
            print("At this temperature, water is a liquid")
        else:
            print("At this temperature, water is a gas")
    else:
        if temperature <= 273:
            print("At this temperature, water is a solid")
        elif temperature > 273 and temperature < 373:
            print("At this temperature, water is a liquid")
        else:
            print("At this temperature, water is a gas")


main()
