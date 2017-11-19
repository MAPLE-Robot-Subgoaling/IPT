def main():
    temp = float ( input ( "Please enter the temperature: " ))
    tempUnit = input ( "Please enter 'C' for Celsius, or 'K' for Kelvin: " )
    FREEZING_CELSIUS = 0
    BOILING_CELSIUS = 100
    FREEZING_KELVIN = 273.15
    BOILING_KELVIN = 373.15
    if temp > FREEZING_CELSIUS and temp < BOILING_CELCIUS and tempUnit == "C" :
        print ("At this temperature, water is a liquid.")
    elif temp <= FREEZING_CELSIUS and tempUnit == "C" :
        print ("At this temperature, water is a solid.")
    elif temp >= BOILING_CELSIUS and tempUnit == "C" :
        print ("At this temperature, water is a gas.")
    elif temp > FREEZING_KELVIN and temp < BOILING_KELVIN and tempUnit == "K" :
        print ("At this temperature, water is a liquid.")
    elif temp <= FREEZING_KELVIN and tempUnit == "K" :
        print ("At this temperature, water is a solid.")
    elif temp >= BOILING_KELVIN and tempUnit == "K" :
        print ("At this temperature, water is a gas.")
main()
