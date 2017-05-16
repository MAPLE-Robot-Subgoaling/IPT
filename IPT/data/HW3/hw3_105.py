

def main():

    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ").upper()

    C_TO_K = 273.15

    if scale == "K":
        ctemp = temp - C_TO_K
    else:
        ctemp = temp
    
    if ctemp <= 0:
        print ("At this temperature, water is a (frozen) solid.")
    elif ctemp <100:
        print ("At this temperature, water is a liquid.")
    else:
        print ("At this temperature, water is a gas.")
            

main()
