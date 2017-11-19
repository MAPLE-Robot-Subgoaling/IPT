def main():
    temperature = float(input("Please enter the temperature:"))
    units = input("Please enter 'C' for Celcius or 'K' for Kelvin:")
    if units == "K":
        ctemp = temperature - 273.2
        if ctemp <= 0:
            print ("At this temperature, water is a (frozen) solid.")
        elif ctemp > 0 and ctemp < 100:
            print ("At this temperature, water is a liquid.")
        else:
            print ("At this temperature, water is a gas.")
    elif units == "C":
        ctemp = temperature
        if ctemp <= 0:
            print ("At this temperature, water is a (frozen) solid.")
        elif ctemp > 0 and ctemp < 100:
            print ("At this temperature, water is a liquid.")
        else:
            print ("At this temperature, water is a gas.")
    else:
        print ("Choose 'C' or 'K'")
main()
