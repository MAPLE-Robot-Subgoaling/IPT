def main():
    temp = float(input("Please enter the temperature: "))
    typetemp = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin"))
    if typetemp  == "C":
        if temp >= 100:
            print("At this temperature, water is a gas")
        if temp <= 0:
            print("At this temperature, water is a (frozen) solid")
        if temp > 0 and temp < 100:
            print("At this temperature, water is  a liquid")
    elif typetemp  == "K":
        if temp >= 373.2:
            print("At this temperature, water is a gas")
        if temp <= 273.2:
            print("At this temperature, water is a (frozen) solid")
        if temp > 273.2 and temp < 373.2:
            print("At this temperature, water is a liquid")
main()
