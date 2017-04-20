
def main():

    userTemp = float(input("Please enter the temperature: "))
    userDegrees = input("Please enter 'C' for Celcius or 'K' for Kelvin: ")
    if userDegrees == 'K':
        if userTemp <= 273:
            print("At this temperature, water is a solid.")
        elif userTemp >= 373:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if userTemp <= 0:
            print("At this temperature, water is a solid.")
        elif userTemp >= 100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")

main()
