def main():
    SOLID_STATE = float(0)
    GAS_STATE = float(100)
    KELVIN_TO_CELSIUS = float(273.15)
    inputTemp = float(input("Please enter the temperature: "))
    inputTempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if(inputTempScale == "K"):
        tempCelsius = float(inputTemp - KELVIN_TO_CELSIUS)
    else:
        tempCelsius = inputTemp
    if(tempCelsius <= SOLID_STATE):
        print("At this temperature, water is a (frozen) solid.")
    elif(tempCelsius >= GAS_STATE):
        print("At this temperature, water is gas.")
    else:
        print("At this temperature, water is a liquid.")
main()
