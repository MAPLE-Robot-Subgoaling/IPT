def main():
    degrees = float(input("Please enter the temperature:"))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if scale == "C":
        if degrees >= 100:
            print("At this temperature, water is a gas.")
        if degrees > 0 < 100:
            print("At this temperature, water is a liquid.")
        if degrees <= 0:
            print("At this temperature, water is solid.")
    if scale == "K":
        if degrees >= 373.15:
            print("At this temperature, water is a gas.")
        if degrees > 273.15 < 373.15:
            print("At this temperature, water is a liquid.")
        if degrees <= 273.15:
            print("At this temperature, water is a solid.")
main()
