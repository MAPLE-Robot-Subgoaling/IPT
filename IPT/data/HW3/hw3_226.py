
def main():
    temp =float(input("Please enter the temperature: "))
    if input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")=='K':
        temp = temp + 273.15
    if temp <= 0:
        print("At this temperature, water is a solid.")
    elif temp >= 100:
        print("At this temperature, water is a gas.")
    else:
        print("At this temperature, water is a liquid.")
main()

