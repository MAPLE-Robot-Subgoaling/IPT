def main ():
    temp = (float (input ("What is the temperature: ")))
    scale = (str (input ("Please enter 'C' for Celsius or 'K' for Kelvin: ")))
    if (scale == 'C'):
        if (temp >= 100):
            print ("At this temperature, water is a gas.")
        elif (temp <= 0):
            print ("At this temperature, water is a frozen solid.")
        else:
            print ("At this temperature, water is a liquid.")
    else:
        if (temp >= 373.15):
            print ("At this temperature, water is a gas.")
        elif (temp <= 273.15):
            print ("At this temperature, water is a frozen solid.")
        else:
            print ("At this temperature, water is a liquid.")
main () 
