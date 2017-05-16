def main():
    temp = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celcius or 'K' for Kelvin: ")
    if temp > 0 and temp < 100 and tempType == "C":
        print("At this temperature, water is a liquid.")
    elif temp < 0 and tempType == "C":
        print("At this temperature, water is a solid.")
    elif temp > 100 and tempType == "C":
        print("At this temperature, water is a gas.")
    elif temp > 273 and temp < 373 and tempType == "K":
        print("At this temperature, water is a liquid.")
    elif temp > 373 and tempType == "K":
        print("At this temperature, water is a gas.")
    else:
        print("At this temperature, water is a solid.")





main()
