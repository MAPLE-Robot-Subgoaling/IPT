def main():
    temp = float(input("Please enter the temperature: "))
    measure = str(input("Please enter 'C' for Celsius or 'K' for Kelvin: "))
    if measure == "C": 
        if temp <= 0: 
            print("Water at this temperature is a solid.")
        elif temp >= 100:
            print("Water at this temperature is a gas.")
        else:
            print("Water at this temperature is a liquid.")
    else:
        if temp <= 273:
            print("Water at this temperature is a solid.")
        elif temp >= 373:
            print("Water at this temperature is a gas.")
        else:
            print("Water at this temperature is a liquid.")
main()
