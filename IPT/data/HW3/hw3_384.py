
def main():

    tempNum = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if tempType == 'C':
        if tempNum  <= 0:
            print("At this temperature, water is a solid.")
        elif tempNum >= 100:
            print("At this temperature, water is a gas.")
        else: 
            print("At this temperature, water is a liquid.")
    else:
        if tempNum <= 273.15:
            print("At this temperature, water is a solid.")
        elif tempNum >= 373.15:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
main()
