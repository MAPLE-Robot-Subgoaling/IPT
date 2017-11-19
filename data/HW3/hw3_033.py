def main():
    temp = float(input("Please enter the temperature: "))
    tempLetter = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if temp > 100 and tempLetter == 'C':
        print("At this temperature, water is a gas.")
    elif temp < 0 and tempLetter == 'C':
        print("At this temperature, water is a solid.")
    elif temp > 0 and temp < 100 and tempLetter == 'C':
        print("At this temperature, water is a liquid.")
    if temp > 373.16 and tempLetter == 'K':
        print("At this temperature, water is a gass.")
    elif temp < 273.15 and tempLetter == 'K':
        print("At this temperature, water is a solid.")
    elif temp > 273.15 and temp < 373.16 and tempLetter == 'K':
        print("At this temperature, water is a liquid.")
main()
