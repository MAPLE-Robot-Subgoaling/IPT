
def main():

    CELSIUS_FREEZE = 0
    CELSIUS_BOIL = 100
    KELVIN_FREEZE = 273.16
    KELVIN_BOIL = 373.16

    waterTemperature = float(input("Please enter the temperature: "))

    measure = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if measure == 'C':
        if waterTemperature <= CELSIUS_FREEZE:
            print("At this temperature, water is a (frozen) solid.")
        elif waterTemperature < CELSIUS_BOIL:
            print("At this temperature, water is a liquid.")
        elif waterTemperature >= CELSIUS_BOIL:
            print("At this temperature, water is a gas.")

    elif measure == 'K':
        if waterTemperature <= KELVIN_FREEZE:
            print("At this temperature, water is a (frozen) solid.")
        elif waterTemperature < KELVIN_BOIL:
            print("At this temperature, water is a liquid.")
        elif waterTemperature >= KELVIN_BOIL:
            print("At this temperature, water is a gas.")
main()
