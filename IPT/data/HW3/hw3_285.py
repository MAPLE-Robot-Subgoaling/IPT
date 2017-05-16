def main():
    temp = float(input("What is the temperature?"))
    unit = input("What measurement is being used(C/K)?")
    if unit == "C":
        if temp <= 0:
            print("This water is a solid.")
        elif temp <= 100:
            print("This water is a liquid.")
        else:
            print("This water is a gas.")
    else:
        if temp <= 273.15:
            print("This water is solid.")
        elif temp <= 373.15:
            print("This water is liquid.")
        else:
            print("This water is a gas.")
main()
