def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if(scale == "C"):
        boilingPoint = 100
        freezingPoint = 0
    else:
        boilingPoint = 373.15
        freezingPoint = 273.15
    if(temp <= freezingPoint):
        state = "(frozen) solid."
    elif(temp >= boilingPoint):
        state = "gas."
    else:
        state = "liquid."
    print("At this temperature, water is a", state)
main()
