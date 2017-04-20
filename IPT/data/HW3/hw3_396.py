

def main():
    theTemp = float(input("Please enter the temperature: "))
    theMetric = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if theMetric == "C":
        if theTemp < 0:
            print("At this temperature, water is a (frozen) solid.")
        elif theTemp >= 100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")

    elif theMetric == "K":
        if theTemp < 273.2:
            print("At this temperature, water is a (frozen) solid.")
        elif theTemp >= 373.2:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")


main()
