
def main():

    degreesNum = float(input("please enter the temperature of the water: "))
    degreesType = str(input("what type of measurement is that temperature in? "))
    if degreesType == "K" and degreesNum >= 373.0:
        print("at this temperature, water is a gas")
    if degreesType == "K" and degreesNum <= 273.0:
        print("at this temperature, water is a solid")
    if degreesType == "K" and degreesNum < 373.0 and degreesNum > 273.0:
        print("at this temperature, water is a liquid")
    if degreesType == "C" and degreesNum >= 100.0:
        print("at this temperature, water is a gas")
    if degreesType == "C" and degreesNum <= 0.0:
        print("at this temperature, water is a solid")
    if degreesType == "C" and degreesNum < 100.0 and degreesNum > 0.0:
        print("at this temperature, water is a liquid")

main()

        
