

def main():
    
    CELSIUS_CONVERSION = 273.15 # Constant added to change Celsius to Kelvin
    K_MELT_TEMP        = 273.15 # Water melting temperature in Kelvin
    K_BOIL_TEMP        = 373.15 # Water boiling temperature in Kelvin

    temp  = float(input("Please enter the temperature: "))
    scale = input("Please enter \"C\" for Celsius, or \"K\" for Kelvin: ")

    if scale == "K":
        k_temp = temp
    
    elif scale == "C":
        k_temp = temp + CELSIUS_CONVERSION
    
    else:
        print("Error: please enter only \"C\" for Celsius or \"K\" for Kelvin")
        exit()
    
    
    if k_temp < 273.15:
        state = "solid"
    
    elif k_temp < 373.15:
        state = "liquid"

    else:
        state = "gas"


    print("At this temperature, water is a", state)

main()
