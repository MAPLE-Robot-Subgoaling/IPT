def main():
    Temperature=float(input("Please enter the temperature:"))
    Unit_Measure=input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if (Unit_Measure=="K"):
         C= Temperature-273.15
         if(C<=0):
             print("At this temperature, water is a (frozen) solid.")
         if(C<=99):
             print("At this temperature, water is a liquid.")
         if(C>=100):
             print("At this temperature, water is a gas.")
    else:
        if(Unit_Measure=="C"):
            if(Temperature<=0):
                print("At this temperature, water is a (frozen) solid.")
            if(Temperature<=99):
                print("At this temperature, water is a liquid.")
            if(Temperature>=100):
                print("At this temperature, water is a gas.")
main()
