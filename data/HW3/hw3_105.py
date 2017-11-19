def main():
    temp = float(input("Please enter the temperature: "))
    scale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if scale == 'C':
        cfreeze = 0
        cboil = 100
        if temp <= cfreeze:
            print("At this temperature, water is a (frozen) solid.")
        elif temp > cfreeze and temp < cboil:
            print("At this temperature, water is a liquid.")
        elif temp >= cboil:
            print("At this temperature, water is a gas.")
    elif scale == 'K':
        kfreeze = 273.15
        kboil = 373.15
        if temp <= kfreeze:
            print("At this temperature, water is a (frozen) solid.")
        elif temp > kfreeze and temp < kboil:
            print("At this temperature, water is a liquid.")
        elif temp >= kboil:
            print("At this temperature, water is a gas.")
main()
