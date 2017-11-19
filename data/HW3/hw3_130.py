def main():
    BOILING_POINT_CELSIUS = 100
    FREEZING_POINT_CELSIUS = 0
    BOILING_POINT_KELVIN = 373.2
    FREEZING_POINT_KELVIN = 273.2
    temperature = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if (scale == "C"):
        if (temperature >= BOILING_POINT_CELSIUS):
            print("At this temperature, water is a gas.")
        elif (temperature <= FREEZING_POINT_CELSIUS):
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if (temperature >= BOILING_POINT_KELVIN):
            print("At this temperature, water is a gas.")
        elif (temperature <= FREEZING_POINT_KELVIN):
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
main()
