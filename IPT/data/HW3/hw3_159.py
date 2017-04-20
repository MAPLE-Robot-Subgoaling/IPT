

def main():
    print ("This program will help determine what physical state your water is in.")
    temperature = float(input("Please enter the temperature: "))
    celcius = str("C")
    kelvin = str("K")
    tempScale = str(input("Please enter 'C' for Celcius, or 'K' for Kelvin: "))
    freezeCelcius = float("0.0")
    gasCelcius = float("100.0")
    if tempScale == "C":
        if temperature <= freezeCelcius:
            print ("At this temperature, water is a (frozen) solid.")
        elif temperature >= gasCelcius:
            print ("Woooo, that water at this temperature is a gas for sure.")            
        else:
            print ("At this temperature, water is a liquid.")
    freezeKelvin = float("273.15")
    gasKelvin = float("373.15")
    if tempScale == "K":
        if temperature <= freezeKelvin:
            print ("At this temperature, water is a (frozen) solid.")
        elif temperature >= gasKelvin:
            print ("At this temperature, water is a gas.")
        else:
            print ("At this temperature, water is a liquid.")


main()
