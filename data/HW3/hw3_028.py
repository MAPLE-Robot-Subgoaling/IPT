def main():
    unit = input("What unit are you using, enter 'C' for celcius or 'K' for Kelvin")
    temp = float(input("What is the temperature?"))
    if (temp <= 0) and (unit == "C") :
        print("At this temperature, water is a (frozen) solid")
    elif (temp >= 100) and (unit == "C") :
        print("At this temperature, water is a gas")
    elif (temp >0 and temp <100) and (unit == "C"):
        print("At this temperature, water is a liquid")
    elif (temp <= 273.15) and (unit =="K"):
        print ("At this temperature, water is a (frozen) solid.")
    elif (temp >= 373.15) and (unit == "K"):
        print ("At this temperature, water is a gas")
    elif (temp >273.15 and temp <373.15) and (unit == "K"):
        print("At this temperature, water is a liquid")
main()  
