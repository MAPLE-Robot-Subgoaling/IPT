
def main():

    KELVIN_GAS = 373.16
    KELVIN_SOLID = 273.16
    CELSIUS_GAS = 100
    CELSIUS_SOLID = 0
    temp = float(input("Please enter the temperature: "))
    tempSystem = input("Please enter 'C' for Celsius and 'K' for Kelvin: ")
    if tempSystem == 'K':
        if temp >= KELVIN_GAS:
            print ("At this temperature, water is a gas.")
        elif temp <= KELVIN_SOLID:
            print ("At this temperature, water is a (frozen) solid.")
        else:
            print ("At this temperature, water is a liquid.")
    elif tempSystem == 'C':
        if temp >= CELSIUS_GAS:
            print ("At this temperature, water is a gas.")
        elif temp <= CELSIUS_SOLID:
            print ("At this temperature, water is a (frozen) solid.")
        else:
            print ("At this temperature, water is a liquid.")

main()
