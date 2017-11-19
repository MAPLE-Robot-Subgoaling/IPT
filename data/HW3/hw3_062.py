def main():
    temperature = float(input("Please enter the temperature: "))
    scale = input("Please enter C for Celsius and K for Kelvin: ")
    if(scale == "C"):
        if(temperature <= 0):
            print("Water at this temperature is a (frozen) solid.")
        elif(temperature >= 100):
            print("Water at this temperature is a gas.")
        else:
            print("Water at this temperature is a liquid.")
    else:
        if(temperature <= 273.15):
            print("Water at this temperature is a (frozen) solid.")
        elif(temperature >= 373.15):
            print("Water at this temperature is a gas.")
        else:
            print("Water at this temperature is a liquid.")
main()
