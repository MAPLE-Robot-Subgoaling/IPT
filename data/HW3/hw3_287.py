def main():
    temperature = int(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempScale == "C":
        if temperature <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif temperature >= 100:
            print("At this temperature, water is a gas.")
        elif temperature > 100 or temperature < 100:
                print("At this temperature, water is a liquid.")
    if tempScale == "K":
        if temperature <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        elif temperature >= 373.15:
            print("At this temperature, water is a gas.")
        elif temperature > 273.15 or temperature < 373.15:
                print("At this temperature, water is a liquid.")
main()
