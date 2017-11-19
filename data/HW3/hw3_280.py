def main():
    typeTemp = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    typeTemp = str(typeTemp)
    waterTemp = input("Please enter the temperature: ")
    waterTemp = float(waterTemp)
    if typeTemp == "K":
        if waterTemp <= 273.00:
            print("The water is a (frozen) solid")
        elif waterTemp >= 373.00:
            print("The water is a Gas")
        else:
            print("The water is a liquid")
    elif typeTemp == "C":
        waterTemp = int(input("Please enter the temperature: "))
        if waterTemp <= 0.00:
            print("The water is a (frozen) solid")
        elif waterTemp >= 100.00:
            print("The water is a gas")
        else:
            print("The water is a liquid")
    else:
        print("Invalid input.")
main()
