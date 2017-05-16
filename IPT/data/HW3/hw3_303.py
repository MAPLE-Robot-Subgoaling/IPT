def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == 'C':
        freezePoint = 0
        boilPoint = 100
        if temp >= boilPoint:
            print("At this temperature, water is a gas")
        elif temp <= freezePoint:
            print("At this temperature, water is a solid")
        else:
            print("At this temperature, water is a liquid")
    if scale == 'K':
        freezePoint = 273.15
        boilPoint = 373.15
        if temp >= boilPoint:
            print("at this temperature, water is a gas")
        elif temp <= freezePoint:
            print("at this temperature, water is a solid")
        else:
            print("At this temperature, water is a liquid")


main()
    
  
                 
