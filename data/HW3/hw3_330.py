def main():
    temp = float(input("Please enter the temperature: "))
    scale = input('Please indicate "C" for Celcius or "K" for Kelvin: ')
    if scale == "C":
        if temp <= 0:
            print("At", temp, "degrees Celsius, water is a solid.")
        elif temp > 0 and temp <100:
            print("At", temp, "degrees Celsius, water is a liquid.")
        else:
            print("At", temp, "degrees Celsius, water is a gas.")
    elif scale == "K":
        if temp <= 273.15:
            print("At", temp, "Kelvin, water is a solid.")
        elif temp > 273.15 and temp < 373.15:
            print("At", temp, "Kelvin, water is a liquid.")
        else:
            print("At", temp, "Kelvin, water is a gas.")
    else:
        print(scale, "is not a compatible scale for temperature")
main()
