def main():
    tempMag   = float(input("Please enter the temperature: ")) 
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ") 
    FREEZE = 0 
    BOIL = 100 
    KELVIN = "K"
    CELCIUS = "C"
    if tempScale == KELVIN:
        tempConverted = tempMag - 273.15 
    else:
        tempConverted = tempMag 
    if tempConverted <= 0:
        print("At this temperature, water is a (frozen) solid.")
    elif tempConverted >= 100:
        print("At this temperature, water is a gas.")
    else:
        print("At this temperature, water is a liquid.")
main()
