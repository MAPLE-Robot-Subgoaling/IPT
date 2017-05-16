
def main():

    heat = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    
    if scale == "K":
        FREEZ_POINT = 273.00
        BOIL_POINT = 373.00
        if heat <= FREEZ_POINT:
            print("At this temperature, water is a (frozen) solid")
        elif (temperature > FREEZ_POINT) and (temperature < BOIL_POINT):
            print("At this temperature, water is a liquid")
        elif temperature >= BOIL_POINT:
            print("At this temperature, water is a gas")

    elif scale == "C":
        FREEZ_POINT1 = 0.00
        BOIL_POINT1 = 100.00
        if temperature <= FREEZ_POINT1:
            print("At this temperature, water is a (frozen) solid")
        elif (temperature > FREEZ_POINT1) and (temperature < BOIL_POINT1):
            print("At this temperature, water is a liquid")
        elif temperature >= BOIL_POINT1:
            print("At this temperature, water is a gas")

main()
