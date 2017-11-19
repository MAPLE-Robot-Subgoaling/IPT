def main() :
    temperature = float(input("Please enter the temperature "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin ")
    if scale == 'C':
        if temperature >= 100:
            print("At this temperature, water is gas.")
        if temperature <= 0:
            print("At this temperature, water is solid.")
        if temperature > 0 and temperature < 100:
            print("At this temperature, water is liquid.")
    else:
        if temperature >= 373:
            print("At this temperature, water is gas.")
        if temperature <= 273.15:
            print("At this temperature, water is solid.")
        if temperature > 273.15 and temperature < 373:
            print("At this temperature, water is liquid.")
main ()
