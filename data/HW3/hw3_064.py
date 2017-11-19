def main():
    temp = float(input("Please enter the temperature: "))
    tempScale = str(input("Please enter 'C' for Celcius, or 'K' for Kelvin: "))
    if tempScale == 'C' or tempScale == 'c':
        if temp <= 0:
            print("At this temperature, water is a solid (frozen).")
        elif temp > 0 and temp < 100:
            print("At this temperature, water is a liquid.")
        elif temp >= 100:
            print("At this temperature, water is a gas.")
    elif tempScale == 'K' or tempScale == 'k':
        if temp <= 273.16:
            print("At this temperature, water is a solid (frozen).")
        elif temp > 273.16 and temp < 373.16:
            print("At this temperature, water is a liquid.")
        elif temp >= 373.16:
            print("At this temperature, water is a gas.")
main()
