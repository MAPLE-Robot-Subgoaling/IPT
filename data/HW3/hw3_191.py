def main():
    myTemp = float(input("Please enter the temperature: "))
    myScale = input("Please enter 'C' for Celsius, or 'K'for Kelvin: ")
    if (myScale == "C"):
        if (myTemp >= 100):
            print("At this temperature, water is a gas.")
        elif (myTemp < 100 and myTemp > 0):
            print("At this temperature, water is a liquid.")
        elif (myTemp <= 0):
            print("At this temperature, water is a (frozen) solid.")
    elif (myScale == "K"):
        if (myTemp >= 373):
            print("At his temperature, water is a gas.")
        elif (myTemp < 373 and myTemp > 273):
            print("At this temperature, water is a liquid.")
        elif (myTemp <= 273):
            print("At this temperature, water is a (frozen) solid.")
main()
