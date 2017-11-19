def main():
    temperature = input("Please enter the temperature: ")
    temperature = float(temperature)
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == 'C':
        if temperature <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif temperature > 0 and temperature < 100:
            print("At this temperature, water is a liquid.")
        elif temperature >= 100:
            print("At this temperature, water is a gas.")
    elif scale == 'K':
        if temperature <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        elif temperature > 273.15 and temperature < 373.15:
            print("At this temperature, water is a liquid.")
        elif temperature >= 373.15:
            print("At this temperature, water is a gas.")
main()
