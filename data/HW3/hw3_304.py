def main():
    tempNum= int(input("Please enter the temperature: "))
    tempType= input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempNum > 0 and tempNum < 100 and tempType == "C":
        print("At this temperature, water is a liquid.")
    if tempNum > 273 and tempNum < 373 and tempType == "K":
        print("At this temperature, water is a liquid.")
    if tempNum <= 0 and tempType == "C":
        print("At this temperature, water is a frozen solid.")
    if tempNum <= 273 and tempType == "K":
        print("At this temperature, water is a frozen solid.")
    if tempNum >= 100 and tempType == "C":
        print("At this temperature, water is a gas.")
    if tempNum >= 373 and tempType == "K":
        print("At this temperature, water is a gas.")
main()
