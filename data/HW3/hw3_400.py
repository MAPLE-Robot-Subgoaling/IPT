def main():
    temperature = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        if temperature <= 0:
            print("At this temperature, water is solid.")
        elif temperature >= 100:
            print("At this temperature, water is gas.")
        else:
            print("At this temperature, water is liquid.")
    if scale == "K":
        if temperature <= 32:
            print("At this temperature, water is solid.")
        elif temperature >= 212:
            print("At this temperature, water is gas.")
        else:
            print("At this temperature, water is liquid.")
main()
