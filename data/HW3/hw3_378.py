def main() :
    Temp = float(input("Please enter the temperature. "))
    CelorKel = input("Please enter 'C' for Celsius, or 'K' for kelvin: ")
    if CelorKel == "C" :
        if Temp >= 100 :
            print("At this temperature, water is a gas.") 
        elif Temp <= 0 :
            print("At this temperature, water is a solid.")
        elif Temp > 0 and Temp <100 :
            print("At this temperature, water is a liquid.")
    else:
        if Temp <= 273.2 :
            print("At this temperature, water is a solid.")
        elif Temp >= 373.2 :
            print("At this temperature, water is a gas.")
        elif Temp > 273.2 and Temp < 373.2 :
            print("At this temperature, water is a liquid.")
main()
