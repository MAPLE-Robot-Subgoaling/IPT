def main():
    FREEZE_TEMP = 0;
    GAS_TEMP = 100;
    KEL_MOD = 273.15;
    num = float(input("Please enter the temperature: "))
    tempType = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin:"))
    if (tempType == "C"):
        if (num <= FREEZE_TEMP):
            print("At this temperature, water is frozen solid.")
        elif (num >= GAS_TEMP):
            print("At this temperature, water is a gas.")
        else: 
            print("At this temperature, water is a liquid.")
    elif (tempType == "K"):
        if (num <= FREEZE_TEMP + KEL_MOD):
            print("At this temperature, water is a frozen solid.")
        elif (num >= GAS_TEMP + KEL_MOD):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        print("Error! Invalid temperature type!")
main()
