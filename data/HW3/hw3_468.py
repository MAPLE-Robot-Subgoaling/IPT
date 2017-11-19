def main():
    temperature = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        if temperature <= 0:
            state = "(frozen) solid"
        elif temperature >= 100:
            state = "gas"
        else:
            state = "liquid"
    elif scale == "K":
        if temperature <= 273.15:
            state = "(frozen) solid"
        elif temperature >= 373.15:
            state = "gas"
        else:
            state = "liquid"
    print("At",temperature,"degrees",scale,"water is a",state)
main()
