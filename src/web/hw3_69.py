
def main():
    FREEZE = 0
    BOIL = 100
    CONVERT = 273.15
    temp = float(input("Please enter the temperature: "))
    print("Please enter the units...")
    units = str(input("Either 'K' for Kelvin or 'C' for Celcius: "))
    
    if units == 'K' :
        tempCel = temp - CONVERT
    else :
        tempCel = temp

    if tempCel <= FREEZE :
        print("At this temperature, water is a (frozen) solid.")
    elif tempCel < BOIL :
        print("At this temperature, water is a liquid.")
    else :
        print("At this temperature, water is a gas.")

main()
