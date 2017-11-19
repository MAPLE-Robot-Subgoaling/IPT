def main():
    LIQUID_K = 330.2
    GAS_K = 370.20
    GAS_C = 100
    LIQUID_C = 60
    numTemp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'K' for Kelvin, or 'C' for Celsius: ")
    if scale == 'K':
        if numTemp >= GAS_K:
            print("At this temperature, water is gas!")
        elif numTemp >= LIQUID_K:
            print("At this temperature, water is liquid!")
        else:
            print("At this temperature, water is solid!")
    elif scale == 'C':
        if unitTemp > GAS_C:
            print("At this temperature, water is gas!")
        elif unitTemp > LIQUID_C:
            print("At this temperature, water is liquid!")
        else:
            print("At this temperature, water is solid!")
main()
