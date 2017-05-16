
def main():
    BOILING_POINT_IN_KELVIN = 373.15
    FREEZING_POINT_IN_KELVIN = 273.15



    temp = float( input( "Please enter the temperature: " ) )
    scale = input( "Please enter 'C' for Celsius, or 'K' for Kelvin: " )


    
    if scale == "C":
        temp = temp + FREEZING_POINT_IN_KELVIN    



    if temp <= FREEZING_POINT_IN_KELVIN:
        print("At this temperature, water is a (frozen) solid.")


    elif temp > FREEZING_POINT_IN_KELVIN and temp < BOILING_POINT_IN_KELVIN:
        print("At this temperature, water is a liquid.")

        
    elif temp >= BOILING_POINT_IN_KELVIN:
        print("At this temperature, water is a gas.")

main()
