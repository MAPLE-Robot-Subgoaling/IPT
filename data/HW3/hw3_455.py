CELSIUS_FREEZING = 0
CELSIUS_BOILING = 100
KELVIN_FREEZING = 273
KELVIN_BOILING = 373
def main():
    temp = int(input("Please enter the temperature: "))
    scale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if scale == "C":
        if temp <= CELSIUS_FREEZING:
            print("At this temperature, water is a frozen solid. ")
        elif temp >= CELSIUS_BOILING:
            print("At this temperature, water is a gas. ")
        elif temp > CELSIUS_FREEZING and temp < CELSIUS_BOILING:
            print("At this temperature, water is a liquid. ")
    if scale == "K":
        if temp <= KELVIN_FREEZING:
            print("At this temperature, water is a frozen solid. ")
        elif temp >= KELVIN_BOILING:
            print("At this temperature, water is a gas. ")
        elif temp > KELVIN_FREEZING and temp < KELVIN_BOILING:
            print("At this temperature, water is a liquid. ")
main()
