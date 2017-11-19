def main ():
    temp     = float(input("Please enther the temperature: "))
    typeTemp = input("Please enter 'C' for celsius, or 'K' for Kelvin ")
    if temp > 0 and temp < 100 and typeTemp == 'C':
        print ("At this temperature, water is a liquid")
    elif temp > 100 and typeTemp == 'C':
        print ("At this temperature, water is a gas")
    elif temp < 0 and typeTemp == 'C':
        print ("At this temperature, water is a solid")
    elif temp == 0 and typeTemp == 'C':
        print ("At this temperature, water is at its freezing point")
    elif temp == 100 and typeTemp == 'C':
        print ("At this temperature, water is at its boiling point")
    if temp > 273.16 and temp < 373.16 and typeTemp == 'K':
        print ("At this temperature, water is a liquid")
    elif temp > 373.16 and typeTemp == 'K':
        print ("At this temperature, water is a gas")
    elif temp < 273.16 and typeTemp == 'K':
        print ("At this temperature, water is a solid")
    elif temp == 273.16 and typeTemp == 'K':
        print ("At this temperature, water is at its freezing point")
    elif temp == 373.16 and typeTemp == 'K':
        print ("At this temperature, water is at its boiling point") 
main()
