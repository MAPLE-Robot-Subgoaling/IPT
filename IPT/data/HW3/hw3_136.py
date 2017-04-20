
def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        if temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif temp >= 100:
            print("At this temperature, water is a gas.")
        elif temp > 0 and temp < 100:
            print("At this temperature, water is a liquid.")
    if scale == "K":
        if temp <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        elif temp >= 373.15:
            print("At this temperature, water is a gas.")
        elif temp > 273.15 and temp < 373.15:
            print("At this temperature, water is a liquid.")

main()
        
