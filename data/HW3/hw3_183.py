def main():
    FREEZING_POINT_C = 0
    BOILING_POINT_C = 100
    FREEZING_POINT_K = 273.15
    BOILING_POINT_K = 373.15
    temp = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius or 'K' for Kelvin (case sensitive): ")
    if tempScale == "C":
        if temp <= FREEZING_POINT_C:
            print("At this temperature, water is a solid.")
        elif temp >= BOILING_POINT_C:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    elif tempScale == "K":
        if temp <= FREEZING_POINT_K:
            print("At this temperature, water is a solid.")
        elif temp >= BOILING_POINT_K:
            print("At this temperature, water is a gas")
        else:
            print("At this temperature, water is a liquid.")
    else: 
        print("User did not choose 'C' or 'K'")
main()
