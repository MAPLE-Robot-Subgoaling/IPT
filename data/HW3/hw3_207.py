def main():
    userTemp = float(input("Please enter the temperature: "))
    unitScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if unitScale == "C":
        if userTemp <= 0:
            print("At this temperature, water is a solid.")
        elif userTemp >= 100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, waster is a liquid.")
    else:
        if userTemp <= 273.2:
            print("At this temperature, water is a solid.")
        elif userTemp >= 373.2:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, waster is a liquid.")
main()
