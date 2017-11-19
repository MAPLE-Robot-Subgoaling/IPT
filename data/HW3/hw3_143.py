def main():
    TEMP_SOLID = 0
    TEMP_GAS = 100
    ABSOLUTE_ZERO = -273.15
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if (scale == "K"):
        temp = temp + ABSOLUTE_ZERO
    if (temp <= TEMP_SOLID): 
        print("At this temperature, water is a (frozen) solid. ")
    elif (temp >= TEMP_GAS): 
        print("At this temperature, water is a gas. ")
    else:
        print("At this temperature, water is a liquid. ")
main()
