def main():
    temp=float(input("Please enter the temperature: "))
    unit=input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    if unit=="C":
        if temp<=0:
            print("At this temperature, water is a solid.")
        elif temp>=100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liguid.")
    elif unit=="K":
        if temp<=273.15:
            print("At this temperature, water is a solid.")
        elif temp>=373.15:
             print("At this temperature, water is a gas.")
        else:
             print("At this temperature, water is a liguid.")
main()
