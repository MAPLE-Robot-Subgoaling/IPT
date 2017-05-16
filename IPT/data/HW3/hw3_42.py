
MELTING_POINT_C = 0.0
MELTING_POINT_K = 273.15
BOILING_POINT_C = 100
BOILING_POINT_K = 373.15

def main():
    temp = float(input("Please enter the temperature: "))
    measure = input("Please enter 'C' for Celsius and 'K' for Kelvin: ")
    
    if measure == "C":
        if temp <= MELTING_POINT_C:
            print("At this temperature, water is a solid.")
        elif temp > MELTING_POINT_C and temp < BOILING_POINT_C:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    elif measure == "K":
        if temp <= MELTING_POINT_K:
            print("At this temperature, water is a solid.")
        elif temp > MELTING_POINT_K and temp < BOILING_POINT_K:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    elif measure == "F":
        print("What do you think this is, America?")
        
main()
