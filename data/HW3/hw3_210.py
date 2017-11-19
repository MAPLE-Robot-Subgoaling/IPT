def main():
    gasCelsius = 100
    solCelsius = 0
    solKelvin = 273.15
    gasKelvin = 373.15
    celsius = "C"
    kelvin = "K"
    userTemp = float(input("Please enter the temperature: "))
    userUnit = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if userUnit == celsius:
        if userTemp <= solCelsius:
            print("At this temperature, water is a solid")
        elif userTemp >= gasCelsius:
            print("At this temperature, water is a gas")
        else:
            print("At this temperature, water is a liquid")
    if userUnit == kelvin:
        if userTemp <= solKelvin:
            print("At this temperature, water is a solid")
        elif userTemp >= gasKelvin:
            print("At this temperature, water is a gas")
        else:
            print("At this temperature water is a liquid")
main()
