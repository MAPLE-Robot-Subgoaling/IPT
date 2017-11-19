def main():
    temp = int(input("please enter a temperature:"))
    scale = input("please enter 'C' for Celsius, or 'K' for Kelvin:")
    if scale == "C":
        if temp  <= 0:
            print("At this temperature, water is frozen")
        elif temp <= 100:
            print("At this temperature, water is liquid")
        else:
            print("At this temperature, water is gas")
    elif scale == "K":
        if temp <= 273:
            print("At this temperature, water is frozen")
        elif temp <= 373:
            print("At this temperature, water is liquid")
        else:
            print("At this temperature, water is gas")
main()
