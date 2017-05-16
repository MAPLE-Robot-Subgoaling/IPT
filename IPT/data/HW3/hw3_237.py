
def main():
    
    temp = float(input("Please enter the temperature: "))

    units = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if units == "K":
        temp = temp - 273.15

    if temp >= 100:
        print("At this temperature, water is a gas.")

    elif temp <= 0:
        print("At this temperature, water is a (frozen) solid.")

    else:
        print("At this temperature, water is a liquid.")

main()
