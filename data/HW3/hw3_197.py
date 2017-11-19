def main():
    K_FREEZING_POINT = 273
    K_BOILING_POINT = 373
    C_FREEZING_POINT = 0
    C_BOILING_POINT = 100
    print()
    print("I will tell you whether water is in its solid, liquid or gaseous state given the temperature and scale (Celsius or Kelvin).")
    print()
    temperature = float(input("Please enter the temperature: "))
    scale = str(input("Please enter \'C\' for Celsius, or \'K\' for Kelvin: "))
    if scale == "C":
        if temperature < C_FREEZING_POINT:
            print("At this temperature, water is a (frozen) solid.")
        elif temperature > C_BOILING_POINT:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else: 
        if temperature < K_FREEZING_POINT:
            print("At this temperature, water is a (frozen) solid.")
        elif temperature > K_BOILING_POINT:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    print()
main()
