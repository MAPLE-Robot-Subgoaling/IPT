
KELVIN = 'K'
CELSIUS = 'C'

WATER_SOLID = "At this temperature, water is a (frozen) solid."
WATER_GAS = "At this temperature, water is a gas."
WATER_LIQUID = "At this temperature, water is a liquid."

CELSIUS_BOILING = 100.0
CELSIUS_FREEZING = 0.0

KELVIN_BOILING = 373.15
KELVIN_FREEZING = 273.15

def main() :

    temperature = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if scale == CELSIUS :
        
        if temperature >= CELSIUS_BOILING :
            
            print(WATER_GAS)
        
        elif temperature <=  CELSIUS_FREEZING :
            
            print(WATER_SOLID)
            
        else :
            
            print(WATER_LIQUID)
            
    elif scale == KELVIN :

        if temperature >= KELVIN_BOILING :
            
            print(WATER_GAS)

        elif temperature <= KELVIN_FREEZING :
            
            print(WATER_SOLID)

        else :

            print(WATER_LIQUID)
        
main()
