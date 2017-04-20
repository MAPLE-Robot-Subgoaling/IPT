
def main():
    K_GAS = 373.15
    K_ICE = 273.15
    C_GAS = 100
    C_ICE = 0
    temp = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if tempType == 'C' and temp >= C_GAS:
        print("At this temperature, water is a gas.")
    elif tempType == 'C' and temp <= C_ICE:
        print("At this temperature, water is a solid.")
    elif tempType == 'C':
        print("At this temperature, water is a liquid.")
    elif tempType == 'K' and temp >= K_GAS:
        print("At this temperature, water is a gas.")
    elif tempType == 'K' and temp <= K_ICE:
        print("At this temperature, water is a solid.")
    elif tempType == 'K':
        print("At this temperature, water is a liquid.")



main()
