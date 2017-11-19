def main():
    temperature = float(input("Please enter the temperature: "))
    temperatureType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if temperatureType == "C":
        if temperature >= 100:
            print("At this temperature, water is a gas.")
        elif temperature > 0:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a solid.")
    elif temperatureType == "K":
        if temperature >= 373.2:
            print("At this temperature, water is a gas.")
        elif temperature > 273.2:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a solid.")
main()
