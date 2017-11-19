def main():
    temp=float(input("Please enter the temperature "))
    unit=str(input("Please enter the units C for Celcius and K for Kelvin:"))
    if unit == "C":
        if temp <= 0:
            print("That is frozen water")
        elif temp >= 100:
            print("That waster is a gas")
        elif temp > 0 and temp < 100:
            print("You have liquid water")
    if unit == "K":
        if temp <= 273:
            print("You have frozen water")
        elif temp >= 373:
            print("You have water as a gas")
        elif temp > 273 and temp < 373:
            print("You have liquid water")
main()
