
def main():
    
    temp = float(input("Please enter the temperature: "))
    tempScale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if (tempScale == "C"):
        if temp >= 100:
            print("At this temperature, water is a gas.")
        elif temp >= 0:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a (frozen) solid.")
    else:
        if temp >= 373.16:
            print("At this temperature, water is a gas.")
        elif temp >= 273.16:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a (frozen) solid.")
main()
