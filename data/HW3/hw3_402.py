def main():
    WATER_FREEZING_TEMP = 0
    WATER_BOILING_TEMP = 100
    Temp=int(input("Please enter the temperature: "))
    TempUnit=input ("please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if TempUnit == "K":
        Temp=Temp-273
    if Temp <= 0:
        print("At this temperature, the water is a solid.")
    elif Temp >= 100:
        print("At this temperature, the water is a gas.")
    else:
        print("At this temperature, the water is a liquid.")
main()
