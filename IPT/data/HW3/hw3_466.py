
CELSIUS_FREEZING_POINT = 0
CELSIUS_BOILING_POINT  = 100

KELVIN_OFFSET          = 273.15

KELVIN_FREEZING_POINT  = CELSIUS_FREEZING_POINT + KELVIN_OFFSET
KELVIN_BOILING_POINT   = CELSIUS_BOILING_POINT  + KELVIN_OFFSET

def main():

    temperature = float(input("Please enter the temperature: "))

    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    
    if scale == "C":


        if temperature < CELSIUS_FREEZING_POINT: 
            print("At this temperature, water is a (frozen) solid.")
        elif temperature < CELSIUS_BOILING_POINT:  
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")

    else:


        if temperature < KELVIN_FREEZING_POINT: 
            print("At this temperature, water is a (frozen) solid.")
        elif temperature < KELVIN_BOILING_POINT:  
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")


main()
