def main():
    temp = float(input("Please enter the temperature:"))
    tempSymbol = input("Please enter 'C'for Celcius or 'K' for Kelvin:")
    if tempSymbol == "C":
        if temp <= 0.0:
            print("At this temperature, water is solid")
        elif (temp > 0.0) and (temp < 100.0):
            print("At this temperature, water is liquid")
        elif temp >= 100.0:
            print("At this temperature, water is gas")
    else:
        if temp <= 273.0:
            print("At this temperature, water is solid")
        elif (temp > 273.0) and (temp < 373.0):
            print("At this temperature, water is liquid")
        elif temp >= 373.0:
            print("At this temperature, water is gas")
main()
