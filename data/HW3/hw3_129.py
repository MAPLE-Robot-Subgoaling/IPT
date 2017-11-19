def main():
    temp = float(input(("Please enter the temperature: ")))
    unit = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if unit == "C" :
        if temp <= 0 :
            print("At this temperature, water is a (frozen) solid.")
        elif temp < 100 :
            print("At this temperature, water is a liquid.")
        elif temp >= 100 :
            print("At this temperature, water is a gas.")
    elif unit  == "K" :
        if temp <= 273.16 :
            print("At this temperature, water is a (frozen) solid.")
        elif temp < 373.16 :
            print("At this temperature, water is a liquid.")
        elif temp >= 373.16 :
            print("At this temperature, water is a gas.")
main()
