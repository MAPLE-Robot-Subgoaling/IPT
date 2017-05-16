
CELSIUS_BOILING_POINT = 100
CELSIUS_FREEZING_POINT = 0
KELVIN_BOILING_POINT = 373.2
KELVIN_FREEZING_POINT = 273.2

def main():

    print("This program will determine the state of water at standard")
    print("pressure (solid, liquid, or gas), based on its temperature.")

    print()

    print("What temperature scale should be used?")
    scale = input("Enter 'C' for Celsius  or 'K' for Kelvin: ")
    
    temperature = float(input("Enter the temperature: "))

    print()

    if scale == "C":
        if temperature > CELSIUS_BOILING_POINT:
            print("At this temperature,  water is a gas.")
        elif temperature < CELSIUS_FREEZING_POINT:
            print("At this temperature,  water is a solid.")
        else: 
            print("At this temperature, water is a liquid.")
    
    elif scale == "K":
        if temperature > KELVIN_BOILING_POINT:
            print("At this temperature,  water is a gas.")
        elif temperature < KELVIN_FREEZING_POINT:
            print("At this temperature, water is a solid.")
        else:
            print("At this temperature, water is a liquid.")

    print()

main()
