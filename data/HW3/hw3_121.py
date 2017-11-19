def main():
    Temperature = float(input("Please enter the temperature: "))
    kind = input("Enter 'K' for kelvin, or 'C' for celcius.")
    if kind == "C":
        if Temperature > 100:
            print("Water is gas")
        elif Temperature < 0:
            print("Water is solid")
        elif (Temperature > 0) and (Temperature < 100):
            print("Water is liquid.")
    if kind == "K":
        Temperature = Temperature -  273.15
        if Temperature > 100:
            print("Water is gas")
        elif Temperature < 0:
            print("Water is solid")
        elif (Temperature > 0) and (Temperature< 100):
            print("Water is liquid.")
main()
