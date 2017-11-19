def main():
    temp=float(input("Please enter the temperature: "))
    scale=str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if scale == "C":
        if(temp <=0):
            print("At this temperature, water is a (frozen) solid.")
        if(temp >=100):
            print("At this temperature, water is a gas.")
        if (temp > 0 and temp < 100):
            print("At this temperature, water is a liquid.")
    if scale == "K":
        if(temp <= 273.16):
            print("At this temperature, water is a (frozen) solid.")
        if(temp >= 373.16):
            print("At this temperature, water is a gas.")
        if(temp > 273.16 and temp <373.16):
            print("At this temperature, water is a liquid.")
main()
