def main():
    temp = int(input("Input a temperature: "))
    kOrC = input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    BOIL_CELCIUS = 100
    FREEZE_CELCIUS = 0
    BOIL_KELVIN = 373
    FREEZE_KELVIN = 273
    if kOrC == "C":
        if temp >= BOIL_CELCIUS:
            print("Your water is a gas")
        elif temp <= FREEZE_CELCIUS:
            print("Your water a solid")
        elif temp < BOIL_CELCIUS and temp > FREEZE_CELCIUS:
            print("You water is a liquid")
        else:
            print("You didn't enter a valid input")
    elif kOrC == "K":
        if temp >= BOIL_KELVIN:
            print("Your water is a gas")
        elif temp <= FREEZE_KELVIN:
            print("Your water a solid")
        elif temp < BOIL_KELVIN and temp > FREEZE_KELVIN:
            print("You water is a liquid")
        else:
            print("You didn't enter a valid input")
    else:
        print("You didn't enter a valid input")
main()
