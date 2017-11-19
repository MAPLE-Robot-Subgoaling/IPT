def main():
    FREEZING_POINT_CELSIUS = 0
    FREEZING_POINT_KELVIN = 273.2
    BOILING_POINT_CELSIUS = 100
    BOILING_POINT_KELVIN = 373.2
    temperatureWater = float(input("Please enter the temperature: "))
    temperatureUnit = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if temperatureUnit == "C":
        if temperatureWater >= BOILING_POINT_CELSIUS:
            print("At this temperature, water is a gas.")
        elif temperatureWater < BOILING_POINT_CELSIUS and temperatureWater > FREEZING_POINT_CELSIUS:
            print("At this temperature, water is a liquid.")
        elif temperatureWater <= FREEZING_POINT_CELSIUS:
            print("At this temperature, water is a solid.")
    elif temperatureUnit == "K":
        if temperatureWater >= BOILING_POINT_KELVIN:
            print("At this temperature, water is a gas.")
        elif temperatureWater < BOILING_POINT_KELVIN and temperatureWater > FREEZING_POINT_KELVIN:
            print("At this temperature, water is a liquid.")
        elif temperatureWater <= FREEZING_POINT_KELVIN:
            print("At this temperature, water is a solid.")
main()
