def main():
    temperature=float(input("Please enter the temperature: "))
    degree=str(input("Please enter 'C' for Celsius and 'K' for Kelvin: "))
    if degree == "C" and temperature <= 0:
        print("At this temperature water is a (frozen) solid")
        exit()
    elif degree == "C" and temperature >= 100:
        print("At this temperature water is a gas")
        exit()
    elif degree == "K" and temperature <= 273.15:
        print("At this temperature water is a (frozen) solid")
        exit()
    elif degree == "K" and temperature >= 373.15:
        print("At this temperature water is a gas")
        exit()
    else:
        print("At this temperature water is a liquid")
        exit()
main()
