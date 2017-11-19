def main():
    celciusBoil = 100
    celciusFreeze = 0
    kelvinBoil = 373.16
    kelvinFreeze = 273.16
    temp = float(input("Please enter the temperature: "))
    degree = input("Please enter 'C' for Celsius, of 'K' for Kelvin: ")
    if (degree == 'C'):
        if (temp >= celciusBoil):
            print("At this temperature, water is a gas.")
        elif (temp > celciusFreeze):
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a (frozen) solid.")
    else:
        if (temp >= kelvinBoil):
            print("At this temperature, water is a gas.")
        elif (temp > kelvinFreeze):
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a (frozen) solid.")
main()
