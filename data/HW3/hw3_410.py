def main():
    temperature = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempType == 'C':
        if temperature <= 0:
            print("At this temperature, water is (frozen) solid.")
        elif temperature >= 100:
            print("At this temperature, water is a gas.")
        elif (temperature > 0) and (temperature < 100):
            print("At this temperature, water is a liquid.")
    elif tempType == 'K':
        if temperature <= 273.15:
            print("At this temperature, water is (frozen) solid.")
        elif temperature >= 373.15:
            print("At this temperature, water is a gas.")
        elif (temperature > 273.15) and (temperature < 373.15):
            print("At this temperature, water is a liquid.")
main()
