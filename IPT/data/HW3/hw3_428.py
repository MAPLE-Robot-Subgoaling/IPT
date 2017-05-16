

def main():
    Temperature = float(input("Please enter the temperature:"))
    TemperatureType = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    
    if TemperatureType == 'C':
        if Temperature <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif Temperature <= 100 :
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    elif TemperatureType == 'K':
        if Temperature <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        elif Temperature <= 373.15 :
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")

main()


