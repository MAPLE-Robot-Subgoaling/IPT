def main():
    GAS_KELVIN = 373.16
    FREEZE_KELVIN = 273.16
    GAS_CELSIUS = 100.0
    FREEZE_CELSIUS = 0.0
    userTemp = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if(tempType == "C"):
        if(userTemp<=0):
            print("At this temperature, water is a frozen solid.")
        elif(userTemp>=100):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    elif(tempType == "K"):
        if(userTemp<=273.16):
            print("At this temperature, water is a frozen solid.")
        elif(userTemp>=373.16):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
main()
