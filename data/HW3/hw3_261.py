temp = float(input("Please enter the temperature: "))
scale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
if (scale == 'C'):
    if (temp >= 100):
        print ("At this temperature, water is a gas.")
    elif (0 < temp < 100):
        print ("At this temperature, water is a liquid.")
    elif (temp <= 0):
        print ("At this temperature, water is a solid.")
elif (scale == 'K'):
    if (temp >= 373.16):
        print ("At this temperature, water is a gas.")
    elif (273.16 < temp < 373.16):
        print ("At this temperature, water is a liquid.")
    elif (temp <= 273.16):
        print ("At this temperature, water is a solid.")
