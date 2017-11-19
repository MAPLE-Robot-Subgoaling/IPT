temperature = float(input("Please enter the temperature:"))
scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
if(scale == "C"):
    if(temperature >= 100):
        print("At this temperature, water is a gas.")
    elif(temperature <= 100 and temperature > 0):
        print("At this temperature, water is a liquid.")
    elif(temperature <= 0):
        print("At this temperature, water is a solid.")
if(scale == "K"):
    if(temperature >= 373.15):
        print("At this temperature, water is a gas.")
    elif(temperature <= 373.15 and temperature > 273.15):
        print("At this temperature, water is a liquid.")
    elif(temperature <= 273.15):
        print("At this temperature, water is a solid.")
