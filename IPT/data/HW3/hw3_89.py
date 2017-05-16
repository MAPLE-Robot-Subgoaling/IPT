
def main():
    temperature = float(input("Please enter the temperature: "))
    tempType    = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ").upper() # For convenience

    if tempType == 'K':
        temperature -= 273 # Cast kelvin values to celsius

    if temperature >= 100:
        print("At this temperature, water is a gas")
    elif temperature > 0:
        print("At this temperature, water is a liquid")
    else:
        print("At this temperature, water is a solid")

main()
