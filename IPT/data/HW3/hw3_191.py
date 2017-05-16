
def main():
    temperature = float(input("Please enter temperature here: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    boilingPoint = 100
    freezingPoint = 0
    boilngPoint2 = 373
    freezingPoint2 = 273
    if scale == "C" :
        if temperature <= freezingPoint:
            print("At this temperature, water is a solid.")
        elif temperature > freezingPoint and temperature < boilingPoint :
            print("At this temperature, water is a liquid.")
        elif temperature >= boilingPoint :
            print("At this temperature, water is a gas.")
        else:
            print("That is not a temperature.")
    elif scale == "K" :
        if temperature <= freezingPoint2 :
            print("At this temperature, water is a solid.")
        elif temperature > freezingPoint2 and temperature < boilingPoint2 :
            print("At this temperature, water is a liquid.")
        elif temperature > boilingPoint2 :
            print("At this temperature, water is a gas.")
        else:
            print("That is not a temperature.")
    else:
        print("That is not a correct scale")
main()
