
def main():
    temperature = float(input("Please enter the temperature: "))
    unit = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if unit == "K":
        temperature = temperature - 273
    if temperature <= 0:
        print("Water is solid at this temperature")
    elif temperature >= 100:
        print("Water is a gas at this temperature")
    else:
        print("Water is a liquid at this temperature")
main()
