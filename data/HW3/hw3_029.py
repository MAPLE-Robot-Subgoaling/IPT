def main():
    temp = float(input("Please enter the temperature: "))
    letter = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if temp <= 0 and letter == 'C':
        print("At this temperature, water is a (frozen) solid.")
    elif temp >= 1 and temp <= 99 and letter == 'C':
        print("At this temperature, water is a liquid.")
    elif temp >= 100 and letter == 'C':
        print("At this temperature, water is a gas.")
    elif temp >= 0 and temp <= 273 and letter == 'K':
        print("At this temperature, water is a (frozen) solid.")
    elif temp > 273 and temp <373 and letter == 'K':
        print("At this temperature, water is a liquid.")
    elif temp > 373 and letter == 'K':
        print("At this temperature, water is a gas.")
main()
