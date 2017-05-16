def main():

    
    unitTemp = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    temperature = input("Please enter the temperature ")
    temperature = float(temperature)
    tempKel=temperature-273.15
    if(unitTemp == "C"):
        if(temperature <= 0):
            print("At this temperature, water is a solid")
    if(unitTemp == "C"):
        if(temperature > 0) and (temperature < 100):
            print("At this temperature, water is a liquid")
    if(unitTemp == "C"):
        if(temperature >= 100):
            print("At this temperature, water is a gas")
    if(unitTemp == "K"):
        if(tempKel <= 0):
            print("At this temperature, water is a solid")
    if(unitTemp == "K"):
        if(tempKel > 0) and (tempKel < 100):
            print("At this temperature, water is a liquid")
    if(unitTemp == "K"):
        if(tempKel >= 100):
            print("At this temperature, water is a gas")


main()
