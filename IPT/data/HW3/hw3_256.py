
FREEZE_POINT_C = 0.0
FREEZE_POINT_K = 273.2
BOIL_POINT_C = 100.0
BOIL_POINT_K = 373.2

def main():
    temp = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if(tempScale == 'C'):
        if(temp <= FREEZE_POINT_C):
            print("At this temperature, water is a (frozen) solid.")
        elif(temp >= BOIL_POINT_C):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if(temp <= FREEZE_POINT_K):
            print("At this temperature, water is a (frozen) solid.")
        elif(temp >= BOIL_POINT_K):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
main()
