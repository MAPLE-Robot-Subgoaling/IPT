def main():
    temperature = float(input("Enter the temperature: "))
    temperatureScale = input("Is it Kelvin (K) or Celsius (C): ")
    if temperatureScale == "K":
        if temperature >= 373.15:
            print("Water is a gas at this temperature.")
        elif 373.15 > temperature > 273.15:
            print("Water is a liquid at this temperature.")
        else:
            print("Water is a solid at this temperature.")
    else:
        if temperature >= 100:
            print("Water is a gas at this temperature.")
        elif 100 > temperature > 0:
            print("Water is a liquid at this temperature.")
        else:
            print("Water is a solid at this temperature.")


main()
