def main():
    temp = float(input("Please enter the temperature: "))
    scale = str(input("Please enter C for Celsius or K for Kelvin."))
    if (temp > 0 and temp < 100) and scale == "C":
        print ("At this temperature, water is a liquid.")
    elif temp <= 0 and scale == "C":
        print ("At this temperature, water is a solid.")
    elif temp >= 100 and scale == "C":
        print ("At this temperature, water is a gas.")
    elif temp >= 373.2 and scale == "K":
        print ("At this temperature, water is a gas.")
    elif (temp > 273.15 and temp < 373.2) and scale == "K":
        print ("At this temperature, water is a liquid.")
    elif temp <= 273.15 and scale == "K":
        print ("At this temperature, water is a solid.")
    if temp < 0 and scale == "K":
        print ("Kelvin cannot be a negative value. Please try again.")
main()
