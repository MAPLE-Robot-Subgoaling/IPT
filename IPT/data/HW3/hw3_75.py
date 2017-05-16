def main():
    temp = float(input("Please enter the temperature: "))
    tempMeasure = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    GAS_IN_KELVINS = 373.15
    GAS_IN_CELSIUS = 100
    SOLID_IN_KELVINS = 273.15
    SOLID_IN_CELSIUS = 0
    if tempMeasure == "K":
        if temp <= SOLID_IN_KELVINS:
            print("Water is a solid at this temperature")
        elif temp >= GAS_IN_KELVINS:
            print("Water is a gas at this temperature")
        else:
            print("Water is a liquid at this temperature")
    elif tempMeasure == "C":
        if temp <= SOLID_IN_CELSIUS:
            print("Water is a solid at this temperature")
        elif temp >= GAS_IN_CELSIUS:
            print("Water is a gas at this temperature")
        else:
            print("Water is a liquid at this temperature")
main()
