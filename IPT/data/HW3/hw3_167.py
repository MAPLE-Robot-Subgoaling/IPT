
def main():

    K_FREEZE = 273.16
    K_BOIL = 373.16
    C_FREEZE = 0
    C_BOIL = 100
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        if temp >= C_BOIL:
            print("At this temperature, water is a gas.")
        elif temp < C_BOIL and temp > C_FREEZE:
            print("At this temperature, water is a liquid.")
        else: 
            print("At this temperature, water is a (frozen) solid.")
    elif scale == "K":
        if temp >= K_BOIL:
            print("At this temperature, water is a gas.")
        elif temp < K_BOIL and temp > K_FREEZE:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a (frozen) solid.")
                 
main()
