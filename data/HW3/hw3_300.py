def main():
    temp=float(input("Please enter the temperature. "))
    temp_type=str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if temp_type=='C':
        if temp<0.0:
            print("At this temperature, water is a frozen solid.")
        elif temp>0.0 and temp<100.0:
            print("At this temperature, water is a liquid.")
        elif temp>100.0:
            print("At this temperature, water is a gas.")
    if temp_type=='K':
        temp=temp-273.15
        if temp<0.0:
            print("At this temperature, water is a frozen solid.")
        elif temp>0.0 and temp<100.0:
            print("At this temperature, water is a liquid.")
        elif temp>100.0:
            print("At this temperature, water is a gas.")
main()
