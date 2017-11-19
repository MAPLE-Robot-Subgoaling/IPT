def main():
    BOILING_PT_C = 100
    FREEZE_PT_C = 0
    K_CONVERS = 273.2
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    if scale == "C":
        temp = temp
        if temp >= BOILING_PT_C:
            print("At this temperature, water is a gas.")
        elif temp <= FREEZE_PT_C:
            print("At this temperature, water is frozen solid.")
        else:
            print("At this temperature, water is a liquid.")
    if scale == "K":
        temp = temp + K_CONVERS
        if temp >= BOILING_PT_C:
            print("At this temperature, water is a gas.")
        elif temp <= FREEZE_PT_C:
            print("At this temperature, water is frozen solid.")
        else:
            print("At this temperature, water is a liquid.")
main()
