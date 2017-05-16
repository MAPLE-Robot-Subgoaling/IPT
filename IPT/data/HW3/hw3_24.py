
FREEZING_POINT_C = 0
BOILING_POINT_C = 100
FREEZING_POINT_K = 273.14
BOILING_POINT_K = 373.14

def main():
    temperature = float(input("Please enter the temperature: "))
    print("capital C or K only")
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempScale == 'C':
        if temperature < FREEZING_POINT_C:
            print(" water is frozen ")
        elif temperature > BOILING_POINT_C:
            print(" water is a gas ")
        elif temperature == FREEZING_POINT_C:
            print(" water is both soild and liquid")
        elif temperature == BOILING_POINT_C:
            print(" water is both liquid and gas")
        else:
            print(" water is a liquid ")
    else:
        if temperature < FREEZING_POINT_K:
            print(" water is frozen ")
        elif temperature > BOILING_POINT_K:
            print("water is a gas ")
        elif temperature == FREEZING_POINT_K:
            print("water is both solid and liquid")
        elif temperature == BOILING_POINT_K:
            print("water is both liquid and gas")
        else:
            print("water is a liquid")
    



 
              

main()
