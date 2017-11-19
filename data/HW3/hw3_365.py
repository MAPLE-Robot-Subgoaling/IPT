def main():
    temperature = float(input("Please enter the temperature"))
    degrees = input("Please enter \"C\" for Celcius or \"K\" for Kelvin.")
    if degrees == "C":
        if temperature <= 0:
            print("Water is a solid at that temperature.")
        elif temperature >= 100:
            print("Water is a gas at that temperature.")
        else:
            print("Water is liquid at that temperature.")
    else:
        if temperature <= 273.2:
            print("Water is a solid at that temperature.")
        elif temperature >= 373.2:
            print("Water is a gas at that temperature.")
        else:
            print("Water is liquid at that temperature.")
main() 
