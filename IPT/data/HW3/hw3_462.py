
def main():
    temp = float(input("Please enter the temperature: "))
    if temp == 60:
        scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
        if scale == "C":
            print("At this tempature, water is a liquid.")
        elif scale == "K":
            print("At this tempature, water is a (frozen) solid.")
    elif temp == 373.2 or 373:
        scale2 = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
        if scale2 == "K":
            print("At this tempature, water is a gas.")
        elif scale2 == "C":
            print("At this tempature, water is a gas")      
main()
