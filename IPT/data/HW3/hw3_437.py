
def main():
    temperature = float(input("Please enter the temperature: "))
    temperatureScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    
    if temperatureScale == 'C':
        if temperature <= 0:
            print("At this temperature, water is a (frozen) solid.")
        if temperature >= 100:
            print("At this temperature, water is a gas.")
        if temperature > 0 and temperature < 100:
            print("At this temperature, water is a liquid.")
    if temperatureScale == 'K':
        if temperature <= 273:
            print("At this temperature, water is a (frozen) solid.")
        if temperature >= 373:
            print("At this temperature, water is a gas.")
        if temperature > 273 and temperature < 373:
            print("At this temperature, water is a liquid.")

main()
