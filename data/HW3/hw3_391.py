def main():
    print()
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter the scale, C for Celsius or K for Kelvin: ")
    if scale == "K":
        temp = temp - 273.15
    if temp <= 0:
        print("At this temperature, water is frozen solid.")
    elif temp < 100: 
        print("At this temperature, water is a liquid")
    else:
        print("At this temperature, water is a gas.")
    print()
main()
