
def main():

    userTemp = float(input("Please enter the temperature:" , ))
    tempType = input("Please enter 'C' for Celsius and 'K' for Kelvin:" , )

    if tempType == "C":
        if userTemp <= 0:
            print("At this temperature, water is a solid.")
        if (userTemp > 0) and (userTemp < 100):
            print("At this temperature, water is a liquid.")
        if userTemp >= 100:
            print("At this temperature, water is a gas.") 
    
    if tempType == "K":
            if userTemp <= 273.15:
                print("At this temperature, water is a solid.")
            if (userTemp > 273.15) and (userTemp < 373.15):
                print("At this temperature, water is a liquid.")
            if userTemp >= 373.15:
                print("At this temperature, water is a gas.")
main()
