C= "Celcius"
K= "Kelvin"
def main():
    temp= float(input("Please enter the temperature: "))
    unitS= input ("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    if unitS=="C" :
        if temp<=0 :
            print ("At this temperature, water is (forzen) solid")
        elif temp>=100 :
            print ("At this temperature, water is gaseous")
        else :
            print ("At this temperature, water is liquid")
    else:
        if temp<= 273.15:
            print ("At this temperature, water is (frozen) solid")
        elif temp>= 373.15:
            print ("At this temperature, water is gaseous")
        else:
            print ("At this temperature, water is liquid")
main()
