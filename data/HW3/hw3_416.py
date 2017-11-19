def main():
    FREEZE_C = 0.0
    BOIL_C = 100.0
    FREEZE_K = 273.15
    BOIL_K = 373.15
    CELCIUS = "C"
    KELVIN = "K"
    temp = float(input("What is the temperature of the water?: "))
    scale = input("What is the scale of the temperature? ('C' for Celcius, 'K' for Kelvin): ")
    if scale == CELCIUS:
        if temp <= FREEZE_C:
            print()
            print("At this temperature, water is a (frozen) solid.")
            print()
        elif temp >= BOIL_C:
            print()
            print("At this temperature, water is a gas.")
            print()
        else:
            print()
            print("At this temperature, water is a liquid.")
            print()
    else:
        if temp<= FREEZE_K:
            print()
            print("At this temperature, water is a (frozen) solid.")
            print()
        elif temp >= BOIL_K:
            print()
            print("At this temperature, water is a gas.")
            print()
        else:
            print()
            print("At this temperature, water is a liquid.")
            print()
main()
