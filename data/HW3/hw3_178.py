def main():
    CELS = "C"
    KELV = "K"
    temp  = float(input("Please enter the temperature: "))
    scale = input("Please enter '" + CELS + "' for Celsius, or '" + KELV + "' for Kelvin: ")
    if scale == CELS:
        if temp >= 100:
            print("At this temperature, water is a gas.")
        elif temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
    if scale == KELV:
        if temp >= 373.16:
            print("At this temperature, water is a gas.")
        elif temp <= 273.16:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
main()
