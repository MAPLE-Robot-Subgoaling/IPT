

def main():

    temp = float(input("Please enter the temperature: "))
    unitTemp = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    
    if unitTemp == "C":
        if temp < 0:
            print("At this temperature, water is a (frozen) solid.")
        elif 0 <= temp < 100:
            print("At this temperature, water is a liquid.")
        elif temp >= 100:
            print("At this temperature, water is a gas.")

    elif unitTemp == "K":
        if temp < 273:
            print("At this temperature, water is a (frozen) solid.")
        elif 273 <= temp < 373:
            print("At this temperature, water is a liquid.")
        elif temp >= 373:
            print("At this temperature, water is a gas.")

main()
