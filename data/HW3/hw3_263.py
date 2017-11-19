def main():
    temperature = float(input("Please enter the temperature: "))
    temperatureScale = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if temperatureScale == "C":
        if temperature <= 0:
            waterState = "solid"
        elif temperature >= 100:
            waterState = "gas"
        else:
            waterState = "liquid"
    else:
        if temperature <= 273.15:
            waterState = "solid"
        elif temperature >=373.15:
            waterState = "gas"
        else:
            waterState = "liquid"
    print("At this temperature, water is a", waterState + ".")
print("")
main()
