def main():
    tempPrompt = float(input("Please enter the temperature: "))
    unitPrompt = str(input("Please enter 'C' for Celsius or 'K' for Kelvin: "))
    if (unitPrompt == 'C'):
        tempPrompt = tempPrompt + 273.15
    else:
        tempPrompt = tempPrompt
    if tempPrompt <= 0:
        print("Not possible. Quit the program and put in a correct temperature next time!")
    elif (0 < tempPrompt < 273.15): 
        print ("At this temperature, water is a solid.")
    elif (273.15 <= tempPrompt < 373.15):
        print ("At this temperature, water is a liquid.")
    else:
        print ("At this temperature, water is a gas.")
main()
