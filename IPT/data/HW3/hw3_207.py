def main():
    SOLID_TEMP_CELSIUS = 0
    GAS_TEMP_CELSIUS = 100
    SOLID_TEMP_KELVIN = 273.15
    GAS_TEMP_KELVIN = 373.15
    tempNum = float(input("Please enter the temperature: "))
    degreeType = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if (degreeType == "C"):
       if (tempNum <= SOLID_TEMP_CELSIUS):
          print("At this temperature, water is a (frozen) solid.")
       elif (tempNum > SOLID_TEMP_CELSIUS and tempNum < GAS_TEMP_CELSIUS):
          print("At this temperature, water is a liquid.")
       else:
           print("At this temperature, water is a gas.")
    else:
        if (tempNum <= SOLID_TEMP_KELVIN):
            print("At this temperature, water is a (frozen) solid.")
        elif (tempNum > SOLID_TEMP_KELVIN and tempNum < GAS_TEMP_KELVIN):
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
main()
