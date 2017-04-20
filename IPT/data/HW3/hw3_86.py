
def main():
    userTemp = float(input("Please enter the temperature: "))
    userConvert = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))

    if (userTemp <= 0.0  and userConvert == 'C') or (userTemp <= 273.2 and userConvert == 'K'):
        print("At this temperature, water is a [frozen] solid.")
    if (userTemp > 0.0 and userTemp < 100.0 and userConvert == 'C') or (userTemp > 273.2 and userTemp < 373.2 and userConvert == 'K'):
        print("At this temperature, water is a liquid.")
    if (userTemp >= 100.0 and userConvert == 'C') or (userTemp >= 373.2 and userConvert == 'K'):
        print("At this temperature, water is a gas.")
    

main()
