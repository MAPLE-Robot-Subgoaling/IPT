def main():
    WATER_FREEZE = 0
    WATER_BOIL = 100
    KELVIN = 273.1
    temp = float(input("Please enter the temperature: "))
    kelvOrCelc = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if(kelvOrCelc == "K"):
        temp = float(temp - KELVIN)
    if(temp < WATER_FREEZE):
        print("At this temperature, water is a (frozen) solid.")
    elif(temp > WATER_BOIL):
        print("At this temperature, water is a gas.")
    else:
        print("At this temperature, water is a liquid.")
main()
