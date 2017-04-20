
def main():
    temp = input("Please enter the temperature: ")
    temp = float(temp)
    CelorKel = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if CelorKel == "C":
        if temp >= 100:
            print("At this temperature, water is a gas.")
        elif temp > 0:
            print("At this temperature, water is a liquid.")
        elif temp <= 0:
            print("At this temperature water is a (frozen) solid.")
    if CelorKel == "K":
        if temp >= 373:
            print("At this temperature, water is a gas.")
        elif temp >= 274:
            print("At this temperature, water is a liquid.")
        elif temp <= 273:
            print("At this temperature water is a (frozen) solid.")

main()

