
def main() :
    temp = int(input("Please enter the temperature:" ))
    units = input("Please enter 'C' for Celsius, or 'K' for Kelvin:" )
    if units == 'C':
        if temp<=0:
            print("At this temperature, water is solid")
        if 1<=temp<=99:
            print("At this temperature, water is a liquid")
        if  temp>=100:
            print("At this temperature, water is a gas")

    if units == 'K':
            if  temp<=273:
                print("At this temperature, water is a solid")
            if  274<=temp<=372:
                print("At this temperature, water is a liquid")
            if  temp>=373:
                print("At this temperature, water is a gas")
main()
