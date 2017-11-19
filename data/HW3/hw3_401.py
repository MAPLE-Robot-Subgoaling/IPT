def main():
    temp = float(input("Please enter the temperature: "))
    tempMeasure = input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    if tempMeasure=="C":
        if temp<=0:
            print("At this temperature, water is a (frozen) solid.")
        elif temp>0 and temp<100:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas. ")
    else:
        if temp<=273.16:
            print("At this temperature, water is a (frozen) solid.")
        elif temp>273.16 and temp<373.16:
            print("At this temperature, water is a liquid.")
        else: 
            print("At this temperature, water is a gas.")
main()
