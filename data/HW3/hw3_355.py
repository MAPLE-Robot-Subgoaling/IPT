def main():
    temp = int(input(" Please enter the temperature: "))
    units = str(input(" Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if temp <= 0 and units == 'C' :
       print("At this temperature, water is a (frozen) solid.")
    elif 100 > temp > 0 and units == 'C' :
       print(" At this temperature, water is a liquid.")
    elif temp >= 100 and units == 'C' :
       print(" At this temperature, water is a gas.")
    if temp <= 273.16 and units == 'K' :
        print(" At this temperature, water is a (frozen) solid.")
    elif 373.16 > temp > 273.16 and units == 'K' :
        print(" At this temperature, water is a liquid.")
    elif temp >= 373.16 and units == 'K' :
        print(" At this temperature, water is a gas.")
main()
