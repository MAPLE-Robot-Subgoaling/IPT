
def main():
    print("Please enter the temperature:")
    tempIn = float(input())
    print("Please enter 'C' for Celsius, or 'K' for Kelvin")
    tempType = input()

    if(tempType == "C"):
        if tempIn >= 100:
            print("At this temperature, water is a gas")
        elif tempIn <= 0:
            print("At this temperature, water is a solid")
        else:
            print("At this temperature, water is a liquid")

    if(tempType == "K"):
        if tempIn >= 373:
            print("At this temperature, water is a gas")
        elif tempIn >= 273:
            print("At this temperature, water is a solid")
        else:
            print("At this temperature, water is a liquid")
    
main()
