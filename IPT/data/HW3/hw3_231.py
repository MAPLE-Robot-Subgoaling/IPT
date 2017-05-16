
def main():

    tempMag   = float(input("Please enter the temperature: ")) #Takes the magnitude(Size) of the temperature without a scale
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ") #asks for what scale the user wants to use
    FREEZE = 0 #degrees celsius
    BOIL = 100 #Degrees celsius
    KELVIN = "K"
    CELCIUS = "C"

    if tempScale == KELVIN:
        tempConverted = tempMag - 273.15 # converts the temperature to celsius if it is given in Kelvin
    else:
        tempConverted = tempMag #Keeps temperature as Celsius

    if tempConverted <= 0:
        print("At this temperature, water is a (frozen) solid.")
    elif tempConverted >= 100:
        print("At this temperature, water is a gas.")
    else:
        print("At this temperature, water is a liquid.")

main()
