def main():
    freezingC=0
    freezingK=273.15
    boilingC=100
    boilingK=373.15
    temp=float(input("Enter the temperature: "))
    unit=str(input("Enter 'C' for Celsius, or 'K' for Kelvin: "))
    if unit=="C":
        if temp<=freezingC:
            print("Solid")
        elif temp>=boilingC:
            print("Gas")
        else:
            print("Liquid")
    else:
        if temp<=freezingK:
            print("Solid")
        elif temp>=boilingK:
            print("Gas")
        else:
            print("Liquid")
main()
