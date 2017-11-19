def main():
    temp = float(input("Please enter the temperaure: "))
    tempUnits = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if ((tempUnits == 'C') and (temp <= 0)) or ((tempUnits == 'K') and (temp <= 273)):
        print("At this temperature, water is a (frozen) solid.")
    elif ((tempUnits == 'C') and (temp >= 100)) or ((tempUnits == 'K') and (temp >= 373)):
        print("At this temperautre, water is a gas.")
    else:
        print("At this temperautre, water is a liquid.")
main()
