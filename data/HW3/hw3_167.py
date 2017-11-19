def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == 'K':
        temp -=  273.15
    if temp < 0:
        print("At this temperature, water is a (frozen) solid.")
    elif temp > 100:
        print("At this temperature, water is a gas.")
    else:
        print("At this temperature, water is a liquid.")
main()
