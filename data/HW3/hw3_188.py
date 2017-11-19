def main():
    temperature = float(input("Please enter the temperature: "))
    tempUnit = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempUnit == "C":  
        if temperature <= 32:
            print("At this temperature, water is a (frozen) solid.")
        elif temperature >= 100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    if tempUnit == "K":
        if temperature <= 273.16:
            print("At this temperature, water is a (frozen) solid.")
        elif temperature >= 373.16:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
main()
