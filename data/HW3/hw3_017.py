def main():
    temp = float(input("Please enter the temperature: "))
    scale = input(print("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if scale == 'C':
        if temp <= 0:
            print("At this temperature, water is a solid")
        elif 0 < temp < 100:
            print("At this temperature, water is a liquid")
        else:
            print("At this temperature, water is a gas")
    else:
        if temp <= 273.15:
            print("At this temperature, water is a solid")
        elif 273.15 < temp < 373.15:
            print("At this temperature, water is a liquid")
        else:
            print("At this temperature, water is a gas")
main()
