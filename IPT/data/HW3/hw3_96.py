def main():
    temp = float(input("Please enter the temperature:"))
    CorK = input("please enter 'C' for celcius, or 'K' for Kelvin:")
    if(CorK == "K"):
        if(temp<=273.15):
            print("At this temperature, water is a (frozen) solid.")
        elif(temp>=373.15):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    if(CorK == "C"):
        if(temp <=0):
            print("At this temperature, water is a (frozen) solid.")
        elif(temp>=100):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid,")
main()
