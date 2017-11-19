def main():
    temperature = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if tempScale == 'K':
        temperature = temperature - 273.15
    if temperature <= 0:
        waterState = "(frozen) solid"
    elif temperature >= 100:
        waterState = "gas"
    else:
        waterState = "liquid"
    print("At this temperature, water is a", waterState)
main()
