
def main():
    temperature = float(input("Please enter the temperature: "))
    temperatureType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if (temperatureType == 'C' and temperature <= 0) or (temperatureType == 'K' and temperature <= 273.15):
        print("At this temperature, water is (frozen) a solid")
        print()
    elif (temperatureType == 'C' and temperature <= 100) or (temperatureType == 'K' and temperature <= 373.15):
        print("At this temperature, water is a liquid")
        print()
    else:
        print("At this temperature, water is a gas")
        print()
main()
