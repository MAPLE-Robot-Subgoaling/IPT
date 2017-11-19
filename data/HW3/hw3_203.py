def main():
    temp=float(input("Please enter the temperature:"))
    tempForm=input("Please enter 'C' for Celsius, or 'K' for Kelvin")
    if tempForm=="K":
        temp=temp-273.15 
    if temp<=0:
        print ("At this temperature, water is a (fronzen) solid.")
    elif temp<=99:
        print ("At this temperature, water is a liquid.")
    elif temp>=100:
        print ("At this temperature, water is a gas.")
main()
