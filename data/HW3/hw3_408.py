def main():
    temp = float(input("Please enter the temperature: "))
    cok = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if cok == "C":
        if temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        if temp > 0 and temp < 100:
            print("At this temperature, water is a liquid.")
        if temp >= 100:
            print("At this temperature, water is a gas.")
    if cok == "K":
        temp = temp - 273.15
        if temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        if temp > 0 and temp < 100:
            print("At this temperature, water is a liquid.")
        if temp >= 100:
            print("At this temperature, water is a gas.")
main()
