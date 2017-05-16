
def main():
    waterTemperature = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        if waterTemperature >= 100:
            print("At this temperature, water is a gas.")
        elif waterTemperature <= 0:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
    elif scale == "K":
        if waterTemperature >= 373.17:
            print("At this temperature, water is a gas.")
        elif waterTemperature <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")


main()
