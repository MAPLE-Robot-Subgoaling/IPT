def main():
    temperature  = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    number = int(input("Please enter the temperature: "))
    if temperature.upper() == "K":
        if number >= 373:
            print("At this temperature, water is a gas.")
        elif number <= 273:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if number >= 100:
            print("At this temperature, water is a gas.")
        elif number <= 0:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
main()    
