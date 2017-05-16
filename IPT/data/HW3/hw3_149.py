
def main():

    temp  = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if((scale == "C" and temp <= 0) or (scale == "K" and temp <= 273.15)):
        print("At this temperature, water is a (frozen) solid.")
    
    elif((scale == "C" and temp >= 100) or (scale =="K" and temp >= 373.2)):
        print("At this temperature, water is a gas.")

    else:
        print("At this temperature, water is a liquid.")

main()
