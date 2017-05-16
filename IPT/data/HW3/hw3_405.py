
def main():

    print("Please enter the temperature: ")
    userTemp = float(input(""))
    print("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    typeTemp = str(input(""))
    if typeTemp == "C":
        if userTemp <= 0:
            print("At this temperature, water is a solid.")
        elif userTemp >= 100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if userTemp <= 273.15:
            print("At this temperature, water is a solid.")
        elif userTemp >= 373.15:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")

main()
