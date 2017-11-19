def main():
    waterTemp = float(input("Please enter the temperature "))
    scaleType = input("Please enter 'C' for Celcius or 'K' for Kelvin")
    FREEZE_C = 0
    FREEZE_K = 273.15
    GAS_C = 100
    GAS_K = 373.15
    if scaleType == "C":
        if waterTemp <= FREEZE_C:
            print("At this temperature, water is a solid")
        elif waterTemp > FREEZE_C and waterTemp < GAS_C:
            print("at this temperature, water is a liquid")
        elif waterTemp >= GAS_C:
            print("At this temperature, water is a gas")
    elif scaleType == "K":
        if waterTemp <= FREEZE_K:
            print("At this temperature, water is a solid")
        if waterTemp > FREEZE_K and waterTemp < GAS_K:
            print("At This temperature, water is a liquid")
        if waterTemp >= GAS_K:
            print("At this temperature, water is a gas")
main()
