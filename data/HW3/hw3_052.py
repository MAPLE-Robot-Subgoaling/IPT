def main():
    waterTemp = float(input("What is the temperature of the water? "))
    print("What is the temperature measured in?")
    tempType = input("Please use 'C' for Celcius and 'K' for Kelvin: ")
    if waterTemp <= 0 and tempType == 'C' or waterTemp <= 273.16 and tempType == 'K':
        print("Water is frozen at this temperature.")
    elif waterTemp >= 100 and tempType == 'C' or waterTemp >= 373.16 and tempType =='K':
        print("Water is in gas state at this temperature.")
    else:
        print("Water is in liquid state at this temperature.")
main()
