def main():
    temperature = float(input("Please enter the temperature:"))
    scale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin:"))
    CFREEZE=(0)
    CBOIL=(100)
    KFREEZE=(273.15)
    KBOIL=(373.15)
    if scale == 'C':
        if temperature <= CFREEZE:
            print("At this temperature, water is a (frozen) solid.")
        if temperature >=CBOIL:
            print("At this temperature, water is a gas.")
        if temperature >CFREEZE and temperature <CBOIL: 
            print("At this temperature, water is a liquid.")
    elif scale == 'K':
        if temperature <= KFREEZE:
            print("At this temperature, water is a (frozen) solid.")
        if temperature >=KBOIL:
            print("At this temperature, water is a gas.")
        if temperature >KFREEZE and temperature <KBOIL: 
            print("At this temperature, water is a liquid.")
    else:
        print("Next time please enter either: 'C' or 'K'")    
main()
