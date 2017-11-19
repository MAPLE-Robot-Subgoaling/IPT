def main():
    temp = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if (tempType == 'C'):
        if (temp >= 100):
            print("The water is gas at this temperature")
        elif (temp >= 0):
            print("The water is liquid at this temperature")
        else:
            print("The water is frozen solid at this temperature")
    elif (tempType == 'K'):
        if (temp >= 373.16):
            print("The water is gas at this temperature")
        elif (temp >= 273.16):
            print("The water is liquid at this temperature")
        else:
            print("The water is frozen solid at this temperature")
main()
