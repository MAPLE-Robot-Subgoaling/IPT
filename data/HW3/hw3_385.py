def main():
    temp = float(input("Please enter the temperature: "))
    unit = input('Please enter "C" for Celsius or "K" for Kelvin: ')
    if unit == "C":
        if temp >= 100:
            print("At this temperature, water is a gas.")
        elif temp <= 0:
            print("At this temperature, water is a solid.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if temp >= 373.15:
            print("At this temperature, water is a gas.")
        elif temp <= 273.15:
            print("At this temperature, water is a solid.")
        else:
            print("At this temperature, water is a liquid")
main()
