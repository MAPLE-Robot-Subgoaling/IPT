
def main():
    
    print("This program determines the state of matter water will be in at the temperature you input, in Celsius or Kelvin.")
    
    tempWater = float(input("Please enter the temperature: "))
    tempType = str(input("Please enter 'C' for celsius, or 'K' for Kelvin: "))
    
    if (tempType == "C"):
        if (tempWater < 0):
            print("At this temperature, water is a (frozen) solid.")
        elif ((tempWater > 0) and (tempWater < 100)):
            print("At this temperature, water is a liquid.")
        elif (tempWater > 100):
            print("At this temperature, water is a gas.")
        elif (tempWater == 0):
            print("At this temperature, water is at its melting point, so it can be either a solid or a liquid, and needs 6.01 kJ per mole taken away or added to change its state of matter to solid or liquid, respectively.")
        elif (tempWater == 100):
            print("At this temperature, water is at its vaporization point, so it can be either a solid or a liquid, and needs 40.65 kJ per mole taken away or added to change its state of matter to liquid or gas, respectively.")
    
    elif (tempType == "K"):
        if (tempWater < 273.15):
                print("At this temperature, water is a (frozen) solid.")
        elif ((tempWater > 273.15) and (tempWater < 373.15)):
            print("At this temperature, water is a liquid.")
        elif (tempWater > 373.15):
            print("At this temperature, water is a gas.")
        elif (tempWater == 273.15):
            print("At this temperature, water is at its melting point, so it can be either a solid or a liquid, and needs 6.01 kJ per mole taken away or added to change its state of matter to solid or liquid, respectively.")
        elif (tempWater == 373.15):
            print("At this temperature, water is at its vaporization point, so it can be either a solid or a liquid, and needs 40.65 kJ per mole taken away or added to change its state of matter to liquid or gas, respectively.")
    

    else:
        print("Please enter 'C' or 'K'.")

main()
