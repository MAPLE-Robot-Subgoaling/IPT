def main():
    print("Hello!")
    waterTemp=int(input("Please enter the temprature:"))
    tempUnit=input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if tempUnit == "C":
        if waterTemp <= 0:
            print("At this temperature, water is a solid.")
        if 0 < waterTemp <= 99:
            print("At this temperature, water is a liquid.")
        if 100 <= waterTemp:
            print("At this temperature, water is a gas.")
    if tempUnit == "K":
        if waterTemp <= 273:
            print("At this temperature, water is a solid.")
        if 273 < waterTemp < 372:
            print("At this temperature, water is a liquid.")
        if 373 <= waterTemp:
            print("At this temperature, water is a gas.")
main()
