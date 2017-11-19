def main():
    userTemp = float(input("Please enter the temperature: "))
    userScale = input("Please enter 'C' for Celcuis, or 'K' for Kelvin: ")
    if userScale == "C":
        if userTemp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif userTemp > 0 and userTemp < 100:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    elif userScale == "K":
        if userTemp <= 273.2:
            print("At this temperature, water is a (frozen) solid.")
        elif userTemp > 273.2 and userTemp < 373.2:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperatue, water is a gas.")
main()
