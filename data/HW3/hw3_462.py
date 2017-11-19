def main():
    temperature = float(input("Please enter the temperature: "))
    tempType    = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ").upper() 
    if tempType == 'K':
        temperature -= 273 
    if temperature >= 100:
        print("At this temperature, water is a gas")
    elif temperature > 0:
        print("At this temperature, water is a liquid")
    else:
        print("At this temperature, water is a solid")
main()
