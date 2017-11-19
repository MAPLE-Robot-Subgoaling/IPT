FREEZING_POINT_OF_WATER_CELSIUS=0
BOILING_POINT_OF_WATER_CELSIUS=100
FREEZING_POINT_OF_WATER_KELVIN=273.15
BOILING_POINT_OF_WATER_KELVIN=373.15
def main():
    temp = float(input("Please enter the temperature: "))
    tempUnit = str(input("Please enter 'C' for Celsius or 'K' for Kelvin: "))
    if tempUnit == "C" :
        if temp < FREEZING_POINT_OF_WATER_CELSIUS :
            print("At this temperature, water is a solid")
        elif temp > BOILING_POINT_OF_WATER_CELSIUS :
            print("At this temperature, water is a gas")
        elif temp == FREEZING_POINT_OF_WATER_CELSIUS :
            print("At this temperature, water is both solid and liquid")
        elif temp == BOILING_POINT_OF_WATER_CELSIUS :
            print("At this temperature, water is both liquid and gas")
        else :
            print("At this temperature, water is a liquid")
    else :
        if temp < FREEZING_POINT_OF_WATER_KELVIN :
            print("At this temperature, water is a solid")
        elif temp > BOILING_POINT_OF_WATER_KELVIN : 
            print("At this temperature, water is a gas")
        elif temp == FREEZING_POINT_OF_WATER_KELVIN :
            print("At this temperature, water is both a solid and liquid")
        elif temp == BOILING_POINT_OF_WATER_KELVIN :
            print("At this temperature, water is both a liquid and gas")
        else :
            print("At this temperature, water is a liquid")
main()
