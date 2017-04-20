
def main():
    temp=float(input("Please enter the temperature: "))
    scale=input("Please enter either 'C' for Celsius or 'K' for Kelvin: ")
    if scale=='K':
        c_temp=temp-273.15
    else:
        c_temp=temp
    if c_temp<=0:
        print("At this temperature, the water is frozen solid.")
    elif c_temp>=100:
        print("At this temperature, the water is a gas.")
    else:
        print("At this tempurature, the water is a liquid.")

main()
