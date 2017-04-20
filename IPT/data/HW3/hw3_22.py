
def main():

    temp = float(input("Please enter the temperature: "))
    unit = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if unit == "K" or unit == "k":
        tempAdj=temp-273
    elif unit == "C" or unit == "c":
        tempAdj=temp
    else:
        print("Improper unit entry. Please try again!")

    if tempAdj <= 0:
        print("At this temperature, water is (frozen) solid.")
    elif tempAdj > 0 and tempAdj < 100:
        print("At this temperature, water is liquid.")
    elif tempAdj >= 100:
        print("At this temperature, water is a gas.")
    else:
        print("Error in the state determination.")

main()
