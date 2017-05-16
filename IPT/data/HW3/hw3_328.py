def main():
    temp = float(input("Please enter the temperature: "))
    tempScales = (input("Please enter 'C' for Celsius or 'K' for Kelvin: "))
    if tempScales == "C":
        if temp < 0.00:
            print("At this temperature, water is a (frozen) solid")
        elif (temp > 0.00 and temp <= 100.00):
            print("At this temperature, water is a liquid")
        else:
            print("At this temperature, water is a gas")
        
    elif tempScale == "K":
        if temp < 273.00:
            print("At this temperature, water is a (frozen) solid")
        elif (temp > 273 and temp <= 373.00):
            print("At this temperature, water is a liquid")
        else:
            print("At this temperature, water is a gas")
        


main()
