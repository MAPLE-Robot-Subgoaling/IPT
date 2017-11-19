def main():
    x = float(input("Please enter the temperature: "))
    y = str(input("Please enter 'C' for Celcius, or 'K' for Kelvin: "))
    if y == 'K':
        if x == 32:
            print("At this temperature, water is solid.")
        elif x == 212:
            print("At this temperature, water is gas.")
        else:
            print("At this temperature, water is liquid.")
    elif y == 'C':
        if x == 0:
            print("At this temperature, water is solid.")
        elif x == 100:
            print("At this temperature, water is gas.")
        else:
            print("At this temperature, water is liquid.")
    else:
        print("That is not a valid character.")
main()
