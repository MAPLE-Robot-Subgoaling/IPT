
def main():
    givenTemp = float(input("Please enter the temperature: "))
    tempType = str(input("Please enter 'C' for Celcius, or 'K' for Kelvin: "))
    if tempType == "C":
        if givenTemp <= 0:
            print("At this temperature, water is frozen solid.")
        elif givenTemp > 0 and givenTemp < 100:
            print("At this temperature, water is liquid.")
        elif givenTemp >= 100:
            print("At this temperature, water is in a gas state.")
    if tempType == "K":
        if givenTemp <= 273.16:
            print("At this temperature< water is frozen solid.")
        elif givenTemp > 273.16 and givenTemp < 373.16:
            print("At this temperature, water is liquid.")
        elif givenTemp >= 373.16:
            print("At this temperature, water is in a gas state.")

main()
