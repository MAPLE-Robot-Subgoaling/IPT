def main():
    temp=float(input("Please enter a temperature: "))
    scale=input("Please enter a 'C' for Celsius or a 'K' for Kelvin: ")
    if scale=="C":
        if temp<=0.0:
            print("At this temperature, water is a solid.")
        elif 0.0<temp and temp<100.0:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    else:
        if temp<273.15:
            print("At this temperature, water is a solid.")
        elif 273.15<temp and temp<373.15:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
main()
