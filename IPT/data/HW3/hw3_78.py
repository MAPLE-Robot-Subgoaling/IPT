
def main():

    tempCheck = float(input("Please enter the temperature: "))
    tempUnit = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempUnit == "C":
        if tempCheck >= 100:
            print("At this temperature water is a gas")
        if tempCheck < 100 and tempCheck > 0:
            print("At this temperature water is a liquid")
        if tempCheck <= 0:
            print("At this temperature water is a solid")
    if tempUnit == "K":
        if tempCheck >= 373:
            print("At this temperature water is a gas")
        if tempCheck < 373 and tempCheck > 273:
            print("At this temperature water is a liquid")
        if tempCheck <= 273:
            print("At this temperature water is a solid")

main()
