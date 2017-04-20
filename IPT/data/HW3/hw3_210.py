
def main():
    temp = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempScale == "C":
        if temp >= 100:
            print("At this temperature, water is a gas.")
        elif temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
    elif tempScale == "K": 
        if temp >= 373:
            print("At this temperature, water is a gas.")
        elif temp <= 273:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At his temperature, water is a liquid.")
main()
