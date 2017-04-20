


def main():

    temperature = float(input("Please enter the temperature:  "))
    scale = input("Please enter 'C' for Celsius, and 'K' for Kelvin:  ")

    if (temperature >= 100 and scale == "C"):
        print("At this temperature, water is a gas.")

    if (temperature >= 1 and temperature < 100 and scale == "C"):
        print("At this temperature, water is a liquid")
    
    if (temperature <= 0 and scale == "C"):
        print("At this temperature, water is a (frozen) solid.")

    if (temperature >= 373.15 and scale == "K"):
        print("At this temperature, water is a gas.")
    
    if (temperature < 373.15 and temperature > 273.15 and scale == "K"):
        print("At this temperature, water is a liquid.")
    
    if (temperature < 273.15 and scale == "K"):
        print("At this temperature, water is a (frozen) solid.")


main()
