def main():
    temp = float(input("Please enter the temurpature: "))
    tempType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempType == "C":
        if temp < 0:
            print("At this tempurature, water is a (frozen) solid.")
        elif temp < 100:
            print("At this tempurature, water is a liquid.")
        else:
            print("At this tempurature, water is a gas.") 
    else:
        if temp < 273.15:
            print("At this tempurature, water is a (frozen) solid.")
        elif temp < 373.15:
            print("At this tempurature, water is a liquid.")
        else:
            print("At this tempurature, water is a gas.")
main()
