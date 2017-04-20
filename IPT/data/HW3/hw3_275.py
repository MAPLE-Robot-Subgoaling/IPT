
def main():
    tempData = float(input("Please enter the temperature:"))
    tempUnit = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin."))
    if (tempUnit == "C" and tempData < 0)or(tempUnit == "K" and tempData < 273):       print("At this temperature, water is a (frozen)solid.")
    elif (tempUnit == "C" and tempData > 0 and tempData < 100) or(tempUnit == "K" and tempData > 273 and tempData < 373):
            print("At this temperature, water is a liquid")
    else:
        print("At this temperature, water is a gas")
main()

