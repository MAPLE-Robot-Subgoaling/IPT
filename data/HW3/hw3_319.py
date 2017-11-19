def main():
    temperature = int(input("Please enter the temperature: "))
    unit = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if unit == "C" and temperature >= 100:
        print("At this temperature, water is a gas.")
    elif unit == "C" and temperature <= 0:
        print("At this temperature, water is a (frozen) solid.")
    elif unit == "C" and temperature > 0 and temperature < 100:
        print("At this temperature, water is a liquid.")
    elif unit == "K" and temperature >= 373:
        print("At this temperature, water is a gas.")
    elif unit == "K" and temperature <= 273:
        print("At this temperature, water is a (frozen) solid.")
    elif unit == "K" and temperature < 373 and temperature > 273:
        print("At this temperature, water is a liquid.")
main()
