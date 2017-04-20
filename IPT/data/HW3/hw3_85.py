def main():
    temperature = float(input("Please enter the temperature "))
    degreetype = input("Please enter 'C' for Celsius, or 'K' for Kelvin ")
    if degreetype == "C":
        if temperature <= 0:
            print("At this temperature, water is a (frozen) solid")
        elif temperature >  0 and temperature < 100:
            print("At this temperature, water is a liquid")
        else:
            print("At this temperature, water is a gas")
    else:
        if temperature <= 273.15:
            print("At this point, water is a (frozen) solid")
        elif temperature > 373.15:
            print("At this point, water is a gas")
        else:
            print("At this point, water is a liquid")
main()
