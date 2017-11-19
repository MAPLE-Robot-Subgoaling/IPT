def main():
    FREEZE_C = 0
    BOIL_C = 100
    FREEZE_K = 273
    BOIL_K = 373
    tempNum = float(input("Please enter the temperature: "))
    tempMes = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempMes == "C" or tempMes == "c":
        if tempNum <= FREEZE_C:
            print("At this temperature, water is a solid.")
        elif tempNum >= BOIL_C:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    elif tempMes == "K" or tempMes == "k":
        if tempNum <= FREEZE_K:
            print("At this temperature, water is a solid.")
        elif tempNum >= BOIL_K:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        print("Please enter a valid measurement.")
main()
