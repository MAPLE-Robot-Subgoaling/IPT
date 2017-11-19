def main (): 
    temp1 = float(input("Please enter the temperature: "))
    celsiusOrKelvin = input ("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if celsiusOrKelvin == "C":
        if (temp1 <= 0.0):
            print ("At this temperature, water is a (frozen) solid.")
        elif (temp1 >0.0 and temp1 < 100.0):
            print ("At this temperature, water is a liquid.")
        elif (temp1 >= 100.0):
            print ("At this temperatue, water is a gas.")
    elif celsiusOrKelvin == "K" :
        if (temp1 <= 273.15):
            print ("At this temperature, water is a (frozen) solid.")
        elif (temp1 > 273.15 and temp1 < 373.15):
            print ("At this temperatue, water is a liquid.")
        elif (temp1 >= 373.15):
            print ("At this temperature, water is a gas.")
    else :
        print("you did not type wether it was a Capital 'C' or 'K' ")
main ()
