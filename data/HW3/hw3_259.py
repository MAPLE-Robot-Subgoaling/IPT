def main():
    temp=float(input("Please input the numerical value of the temperature: "))
    scale=input("Please enter 'C' for Celcius and 'K' for Kelvin. ")
    if scale!="K":
        if temp<=0:
            print("At this temperature, water is frozen.")
        elif temp>=100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if temp<=273.15:
            print("At this temperature, water is frozen.")
        elif temp>=373.15:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
main()
