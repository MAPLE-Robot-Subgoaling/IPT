KELVIN_FREEZING_POINT = 273.16
KELVIN_BOILING_POINT = 373.16
CELSIUS_FREEZING_POINT = 0
CELSIUS_BOILING_POINT = 100
def main():
    temp = float(input("Please enter the temperature: "))
    scale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if scale == "C":
        if temp <= CELSIUS_FREEZING_POINT:
            print("At this temperature, water is a (frozen) solid.")
        elif CELSIUS_FREEZING_POINT < temp < CELSIUS_BOILING_POINT:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    elif scale == "K":
        if temp <= KELVIN_FREEZING_POINT:
            print("At this temperature, water is a (frozen) solid.")
        elif KELVIN_FREEZING_POINT < temp < KELVIN_BOILING_POINT:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
main()
