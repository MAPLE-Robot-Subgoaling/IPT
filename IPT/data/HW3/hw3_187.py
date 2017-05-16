
def main():
    userTemp=float(input("Please enter a temperature:"))
    userScale=input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if userScale=="C":
        if userTemp<=0:
            print("At this temperature, water is a (frozen) solid.")
        elif userTemp>=100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    elif userScale=="K":
        if userTemp<=273.15:
            print("At this temperature, water is a (frozen) solid.")
        elif userTemp>=373.15:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
main()

                       
