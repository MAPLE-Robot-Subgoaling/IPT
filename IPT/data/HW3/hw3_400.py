
def main():

    temp = input("Please enter the temperature: ")
    units = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if units == "C":
        if float(temp) >= 0 and float(temp) < 100:
            print("At this temperature, water will be liquid.")
        elif float(temp) >= 100:
            print("At this temperature, water will be gas.")
        else:
            print("At this temperature, water will be solid.")
    else:
        if float(temp) >= 373.2:
            print("At this temperature, water will be gas.")
        elif float(temp) > 273.2:
            print("At this temperature, water will be liquid.")
        else:
            print("At this temperature, water will be solid.")


main()
