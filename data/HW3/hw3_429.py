def main():
    temp = float(input("Please enter a temperature: "))
    scale = ""
    while (scale != "C") and (scale != "K"):
        scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        FREEZING_POINT = 0
        BOILING_POINT = 100
    elif scale == "K":
        FREEZING_POINT = 273.15
        BOILING_POINT = 373.15
    if temp <= FREEZING_POINT:
        print("At this temperature, water is a solid")
    elif (temp > FREEZING_POINT) and (temp < BOILING_POINT):
        print("At this temperature, water is a liquid")
    elif temp >= BOILING_POINT:
        print("At this temperature, water is a gas")
main()
print()
