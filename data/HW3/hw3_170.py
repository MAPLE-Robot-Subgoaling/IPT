def main():
    temperature = float(input("Please enter the temperature: "))
    stateOfMatter = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if stateOfMatter == "C":
        if temperature <= 0.0:
            print("At this temperature, water is a (frozen) solid.")
        elif temperature >= 100.0:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if temperature <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        elif temperature >= 373.15:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
main()
