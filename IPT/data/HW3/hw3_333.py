
def main():

    temp = float(input("Please enter the temperature: "))
    unit = input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    if unit == "C":
        if temp >= 100:
            print("At this temperature, water is a gas.")
        elif temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
    elif unit == "K":
        if temp >= 373.16:
            print("At this temperature, water is a gas.")
        elif temp <= 273.16:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
main()
