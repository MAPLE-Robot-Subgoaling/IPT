def main():
    userTemp = int(input("Please enter the temperature: "))
    userScale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if userScale == "C":
        if userTemp <= 0:
            print("At this temperature, water is a solid.")
        elif userTemp > 0 and userTemp < 100:
            print("At this temperature, water is a liquid.")
        elif userTemp >= 100:
            print("At this temperature, water is a gas.")
    if userScale == "K":
        if userTemp <= 273:
            print("At this temperature, water is a solid.")
        elif userTemp > 273 and userTemp < 373:
            print("At this temperature, water is a liquid.")
        elif userTemp >= 373:
            print("At this temperature, water is a gas.")
main()
