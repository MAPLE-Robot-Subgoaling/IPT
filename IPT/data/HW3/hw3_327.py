
def main():

    temp = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")

    if(tempType.lower() == 'c'):
        if(temp <= 0):
            print("At this temperature, the water is a (frozen) solid.")
        elif(temp > 0 and temp < 100):
            print("At this temperature, the water is a liquid.")
        elif(temp >= 100):
            print("At this temperature, the water is a gas.")
            
    elif(tempType.lower() == 'k'):
        if(temp <= 273.16):
            print("At this temperature, the water is a (frozen) solid.")
        elif(temp > 273.16 and temp < 373.16):
            print("At this temperature, the water is a liquid.")
        elif(temp >= 373.16):
            print("At this temperature, the water is a gas.")

main()
