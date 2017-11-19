def main():
    GAS_C = 100
    LIQUID_C = 60
    GAS_K = 373.15
    LIQUID_K = 333.15
    temp = float(input("Please enter the temperature "))
    unit = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if unit == 'C':
        if temp > GAS_C:
            print("At this temperature, water is a gas")
        elif temp >= LIQUID_C:
            print("At this temperature, water is a liquid")
        else:
            print("At this temperature, water is a solid")
    elif unit == 'K':
        if temp >= GAS_K:
            print("At this temperature, water is a gas")
        elif temp >= LIQUID_K:
            print("At this temperature, water is a liquid")
        else:
            print("At this temperature, water is a solid")
main()
