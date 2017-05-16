


def main():

    temperature = float(input("What is the temperature?"))
    degree = input("Please enter 'K'for Kelvin or 'C' for Celsius!!")
    if degree == "C" and temperature <= 0:
        print ("Your water is in solid state")
    elif degree == "C" and temperature >= 100:
        print ("Your water is in gas state")
    elif degree == "C" and temperature < 100:
        print ("Your water is in liquid state")
    elif degree == "K" and temperature >= 32:
        print ("Your water is in solid state")
    elif degree == "K" and temperature >= 212:
        print ("Your water is in gas state")
    else:
        print ("Your water is in liquid state")
main()
