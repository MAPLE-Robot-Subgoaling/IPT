
BOIL_PT_K= 373.2
FREZ_PT_K= 273.2
BOIL_PT_C= 100
FREZ_POINT_C= 0

def main():

    temp= float(input("Please enter the temperature:"))
    tempScale= input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if tempScale == "K":
        if temp >= BOIL_PT_K :
            print("At this temperature, water is a gas.")
        if temp < BOIL_PT_K and temp > FREZ_PT_K :
            print("At this temperature, water is a liquid.")
        if temp <= FREZ_PT_K :
            print("At this temperature, water is a solid.")
    if tempScale == "C":
        if temp >= BOIL_PT_C:
            print("At this temperature, water is a gas.")
        if temp < BOIL_PT_C and temp > FREZ_POINT_C:
            print("At this temperature, water is a liquid.")
        if temp <= FREZ_POINT_C:
            print("At this temperature, water is a solid.")

main()
