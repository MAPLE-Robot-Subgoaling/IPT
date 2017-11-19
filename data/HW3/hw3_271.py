def main():
    temperature = float(input("Please enter the temperature: "))
    measurement = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    solid = "At this temperature, water is a (frozen) solid."
    liquid = "At this temperature, water is a liquid."
    gas =  "At this temperature water is a gas."
    if (measurement == "C"):
        if (temperature < 0):
            print (solid)
        elif (temperature >= 0 and temperature < 100):
            print (liquid)
        elif (temperature >= 100):
            print (gas)
    elif (measurement == "K"):
        if (temperature < 273.2):
            print (solid)
        elif (temperature >= 273.2 and temperature < 373.2):
            print (liquid)
        elif (temperature >= 373.2):
            print (gas)
main()
