def main():
    tempType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    tempNum  = float(input("Pease enter temperature: "))
    if tempType == "C":
        if tempNum <= 0:
            print("At this temperature, water is a solid")
        if tempNum > 0 and tempNum < 100:
            print("At this temperature, water is a liquid")
        if tempNum >= 100:
            print("At this temperature, water is a gas")
    if tempType == "K":
        if tempNum <= 273.15:
            print("At this temperature, water is a solid")
        if tempNum > 273.15 and tempNum < 373.15:
            print("At this temperature, water is a liquid")
        if tempNum >= 373.15:
            print("At this temperature, water is a gas")
main()
