CELSIUS_BOILING_POINT = 100
CELSIUS_FREEZING_POINT = 0
KELVIN_BOILING_POINT = 373.16
KELVIN_FREEZING_POINT = 273.16
def main():
    waterTemperature = float(input("Please enter the temperature:"))
    temperatureType = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if temperatureType == "C":
        if waterTemperature <= 100
            print("At this temperature, water is a solid.")
        elif waterTemperature > 0 and waterTemperature < 100:
            print("At this temperature, water is liquid.")
        else:
            print("At this temperature, water is a gas.")
    else:
        if waterTemperature <= 273.16:
            print("At this temperature, water is a solid.")
        elif waterTemperaeture > 273.16 and waterTemperature < 373.16:
            print("At this temperature, water is liquid.")
        else:
            print("At this temperature, water is a gas.")
main()
