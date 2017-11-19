def main():
    temperature = float(input("Please enter the temperature: "))
    scaleType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    C_FROZEN = 0
    C_BOIL = 100
    K_FROZEN = 273
    K_BOIL = 373
    if  scaleType == 'C':
        if temperature <= C_FROZEN:
            print("At this temperature, water is a (frozen) solid.")
            print(" ")
        elif (temperature > C_FROZEN) and (temperature < C_BOIL):
            print("At this temperature, water is a liquid.")
            print(" ")
        else: 
            print("At this temperature, water is a gas.")
            print(" ")
    else:
        if temperature <= K_BOIL:
            print("At this temperature, water is a (frozen) solid.")
            print(" ")
        elif (temperature > K_FROZEN) and (temperature < K_BOIL):
            print("At this temperature, water is a liquid.")
            print(" ")
        else:
            print("At this temperature, water is a gas.")
            print(" ")
main()
