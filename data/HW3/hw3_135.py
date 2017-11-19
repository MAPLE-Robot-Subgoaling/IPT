def main():
    temp=float(input("Please enter the temperature:"))
    tempType=input("please enter 'C' for Celsius, or 'K' for Kelvin:")
    if (tempType == ("C") or tempType == ("K")):
        if tempType == "K":
            temp = temp - 273.15
        if temp < 0:
            print("At this temperature water is solid.")
        elif temp < 100:
            print("At this temperature water is a liquid.")
        else:
            print("At this temperature water is a gas.")
    else:
        print("Error: unknown temperature measurment.")
main()
