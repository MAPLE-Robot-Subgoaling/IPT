def main():
    BOILING_POINT_CELSIUS = 100
    FREEZING_POINT_CELSIUS = 0
    BOILING_POINT_KELVIN = 373.16
    FREEZING_POINT_KELVIN = 273.16
    temperature = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempType == "C":
        if temperature >= BOILING_POINT_CELSIUS:
            print("At this temperature, water is a gas. ")
        elif temperature <= FREEZING_POINT_CELSIUS:
            print("At this temperature, water is a solid. ")
        else:
            print("At this temperature, water is a liquid. ")
    elif tempType == "K":
        if temperature >= BOILING_POINT_KELVIN:
            print("At this temperature, water is a gas. ")
        elif temperature <= FREEZING_POINT_KELVIN:
            print("At this temperature, water is a solid. ")
        else:
            print("At this temperature, water is a liguid. ")
main()
