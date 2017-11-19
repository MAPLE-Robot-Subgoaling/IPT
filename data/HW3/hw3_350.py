def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if (temp <= 0 and scale == "C") or (temp <= 273.16  and scale == "K"):
        print("At this temperature, water is a solid")
    elif (temp >= 100 and scale == "C") or (temp >= 373.16 and scale == "K"):
        print("At this temperature, water is a gas")
    else:
        print("At this temperature, water is a liquid")
main()
