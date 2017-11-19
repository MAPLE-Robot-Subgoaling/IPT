def main():
    temp = float(input("Please enter the temperature:"))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if tempScale == "C":
        if temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif temp > 0 and temp < 100:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    if tempScale == "K":
        if temp <= 200:
            print("At this temperature, water is a (frozen) solid.")
        elif temp > 200 and temp < 373:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
main()
