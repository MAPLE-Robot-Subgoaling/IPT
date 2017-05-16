def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C": 
        if temp<=0:
            print("At this temperature, water is a (frozen) solid.")
        elif temp>=100:
            print("At this temperature, water is a gas.")
        else: 
            print("At this temperature, water is a liquid.")
    else:
        if temp<=273.16: 
            print("At this temperature, water is a (frozen) solid.")
        elif temp>=373.16: 
            print("At this temperature, water is a gas.")
        else: 
            print("At this temperature, water is a liquid.")
main()
