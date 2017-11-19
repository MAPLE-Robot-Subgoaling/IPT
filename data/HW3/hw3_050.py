def main():
    temp=float(input("Please enter the temperature: "))
    degree=input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    if degree=="K":
        temp=temp-273.15
    if temp>=100:
        print("At this temperature, water is a gas.")
    elif temp<=0:
        print("At this temperature, water is a (frozen) solid.")
    else:
        print("At this temperature, water is a liquid.")
main()
