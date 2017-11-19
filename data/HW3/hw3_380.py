def main():
    theTemp = float(input("Please enter the temperature:"))
    theScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if theScale == "C":
        if theTemp <= 0:
            print("At this temperature, water is a solid.")
        elif theTemp >= 0 and theTemp <= 100:
            print("At this temperature, water is a liquid.")
        elif theTemp >= 100:
            print("At this temperature, water is a gas.")
    if theScale == "K":
        if theTemp <= 273:
            print("At this temperature, water is a solid.")
        elif theTemp >= 273 and theTemp <= 373:
            print("At this temperature, water is a liquid.")
        elif theTemp >= 373:
            print("At this temperature, water is a gas.")
main()
