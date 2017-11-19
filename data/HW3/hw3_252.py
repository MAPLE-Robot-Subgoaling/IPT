def main():
    temperature = float(input("Enter temperature: "))
    scale = input("Enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        if temperature >= 100:
            print("At this temperature, water is a gas.")
        elif temperature <= 0:
            print("At this temperature, water is a solid.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if temperature >= 373.16:
            print("At this temperature, water is a gas.")
        elif temperature <= 273.16:
            print("At this temperature, water is a solid.")
        else:
            print("At this temperature, water is a liquid.")
main()
