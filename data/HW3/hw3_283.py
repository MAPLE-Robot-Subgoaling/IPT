def main():
    Temperature=float(input("Please enter the temperature:"))
    Type=input("Please enter 'C' for celsius, or 'K' for Kelvin:")
    if Temperature<=0 and Type=="C":
        print("At this temperature, water is a solid")
    elif Temperature>0 and Temperature<100 and Type=="C":
        print("At this temperature, water is a liquid")
    elif Temperature>=100 and Type=="C":
        print("At this temperature, water is a gas")
    elif Temperature<=273 and Type=="K":
        print("At this temperature, water is a solid")
    elif Temperature>273 and Temperature<373 and Type=="K":
        print("At this temperature, water is a liquid")
    elif Temperature>373 and Type=="K":
        print("At this temperature, water is a gas")
main()
