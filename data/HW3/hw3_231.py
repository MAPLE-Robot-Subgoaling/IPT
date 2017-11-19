def main():
    temp = float(input("Please enter the temperature: "))
    scales = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if scales == "C"  and temp >= 100:
        print("At this temperature, water is a gas.")
    elif scales == "C" and temp > 0 and temp < 100:
        print("At this temperature, water is a liquid.")
    elif scales == "C" and temp <= 0:
        print("At this temperature, water is a (frozen) solid.")
    elif scales == "K" and temp >= 373.15:
        print("At this temperature, water is a gas.")
    elif scales == "K" and temp > 273.15 and temp < 373.15:
        print("At this temperature, water is a liquid.")
    elif scales== "K" and temp <= 273.15:
        print("At this temperature, water is a (frozen) solid.")
main()
