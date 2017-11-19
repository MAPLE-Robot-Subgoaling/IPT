def main ():
    temperature = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if(scale == "C"):
        if(temperature > 99):
            print("At this temperature, water is a gas.")
        elif(temperature > 0):
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a (frozen) solid.")
    else:
        if(temperature >= 373.15):
            print("At this temperature, water is a gas.")
        elif(temperature > 273.15):
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a (frozen) solid.")
main()
