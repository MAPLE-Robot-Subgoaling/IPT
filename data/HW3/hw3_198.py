def main():
    number = float(input("Please enter the temperature: "))
    unit = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if(unit == "C"):
        if(number <= 0):
            print("At this temperature, water is a (frozen) solid.")
        elif(number >= 100):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    if(unit == "K"):
        if(number <= 273):
            print("At this temperature, water is a (frozen) solid.")
        elif(number >= 373):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
main()
