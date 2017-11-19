def main():
    userTemp = float(input("Please enter the temperature:"))
    userScale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin:"))
    BOILING_KELVIN = 373.15
    BOILING_CELSIUS = 100
    FREEZE_KELVIN = 273.15
    FREEZE_CELSIUS = 0
    if (userTemp <= FREEZE_CELSIUS and userScale == "C"):
        print("Water is a solid at this temperature")
    elif (userTemp <= FREEZE_KELVIN and userScale == "K"):
        print("Water is a solid at this temperature")
    elif (userTemp > FREEZE_CELSIUS and userTemp < BOILING_CELSIUS and userScale == "C"):
        print("Water is a liquid at this temperature")
    elif (userTemp > FREEZE_KELVIN and userTemp < BOILING_KELVIN and userScale == "K"):
        print("Water is a liquid at this temperature")
    elif (userTemp >= BOILING_CELSIUS and userScale == "C"):
        print("Water is a gas at this temperature")
    elif (userTemp >= BOILING_KELVIN and userScale == "K"):
        print("Water is a gas at this temperature")
main()
