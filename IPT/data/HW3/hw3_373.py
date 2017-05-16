

def main():
    CELSIUS_BOILING_TEMPERATURE = 100
    CELSIUS_FREEZING_TEMPERATURE = 0
    KELVIN_SOLID_TEMPERATURE = 273.16
    KELVIN_GAS_TEMPERATURE = 373.16
 
    temp = float(input("Please enter the temperature: "))
    scale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    
    if scale == 'C':
        if temp < CELSIUS_FREEZING_TEMPERATURE:
            print("At this temperature, water is a (frozen) solid.")
        elif CELSIUS_BOILING_TEMPERATURE < temp > CELSIUS_FREEZING_TEMPERATURE:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    
    elif scale == 'K':
        if temp < KELVIN_SOLID_TEMPERATURE:
            print("At this temperature, water is a (frozen) solid")
        elif KELVIN_GAS_TEMPERATURE < temp > KELVIN_SOLID_TEMPERATURE:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")

main()
