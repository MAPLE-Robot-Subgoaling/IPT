

BOILING_C = 100
FREEZING_C = 0
BOILING_K = 373
FREEZING_K = 273

def main():

    temp = float(input("Please enter the temperature: "))
    scale = input("Enter 'C' if the temperature is Celsius, 'K' if Kelvin: ")

    if scale == ('C'):
        if temp >= BOILING_C:
            print ("Water is a gas at this temperature.")
        elif temp <= FREEZING_C:
            print ("Water is a solid, ice, at this temperature.")
        else:
            print ("Water is a liquid at this temperature.")

    else:
        if temp >= BOILING_K:
            print ("Water is a gas at this temperature.")
        elif temp <= FREEZING_K:
            print ("Water is a solid, ice, at this temperature.")
        else:
            print ("Water is a liquid at this temperature.")


main()
