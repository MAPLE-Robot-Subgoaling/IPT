
def main():

    input1 = float(input("Please enter the temperature: "))
    if str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")) == "C":
        if input1 > 0:
            print("At this temperature, water is a liquid.")
        elif input1 >= 100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a (frozen) solid.")
    else:         
        if input1 > 273.15:
            print("At this temperature, water is a liquid.")
        elif input1 >= 373.15:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a (frozen) solid.")


main()
