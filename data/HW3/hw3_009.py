def main():
    temp = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if (tempType == 'C'):
        if (temp <= 0):
            print ("At this temperature, water is a (frozen) solid.")
        elif (temp > 0) and (temp < 100):
            print ("At this temperature, water is a liquid.")
        elif (temp >= 100):
            print ("At this temperature, water is a gas.")
    elif (tempType == 'K'):
        if (temp <= 273.26):
            print ("At this temperature, water is a (frozen) solid.")
        elif (temp > 273.26) and (temp < 373.16):
            print ("At this temperature, water is a liquid.")
        elif (temp >= 373.16):
            print ("At this temperature, water is a gas.")
    else:
        print ("I don't recognize this temperature.")
main()
