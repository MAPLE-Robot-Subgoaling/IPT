
def main():
    
    temperature = float(input("Please enter the temperature: "))
    scale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if scale == "C":
        if temperature <= 0:
            print("At this temperature, water is (frozen) solid.")
        elif temperature > 0 and temperature < 100:
            print("At this temperature, water is a liquid.")
        elif temperature >= 100:
            print("At this temperature, water is a gas.")
    elif scale == "K":
        if temperature <= 273.16:
            print("At this temperature, water is (frozen) solid.")
        elif temperature > 273.16 and temperature < 373.16:
            print("At this temperature, water is a liquid.")
        elif temperature >= 100:
            print("At this temperature, water is a gas.")
    

main()
