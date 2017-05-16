

def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if "C" == scale and temp > 100.00:
        print("At this temperatue, water is a gas.")
    elif "K" == scale and temp > 373.15:
        print("At this temperature, water is a gas.")
    elif "C" == scale and temp > 0.00 and temp < 100.00:
        print("At this temperature, water is a liquid.")

    elif"K" == scale and temp > 273.15 and temp < 373.15:
        print("At this temperature, water is a liquid.")
    else:
        print("At this temperature, water is a solid.")
    


main()
