
def main():
    temp = int(input("Please enter the temperature: "))
    celsiusKelvin = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if celsiusKelvin == "C" and temp <= 0:
        print("At this temperature, water is a (frozen) solid.")
    if celsiusKelvin == "K" and temp <= 273:
        print("At this temperature, water is a (frozen) solid.")
    if celsiusKelvin == "C" and temp > 0 and temp < 100:
        print("At this temperature, water is a liquid.")
    if celsiusKelvin == "K" and temp > 273 and temp < 373:
        print("at this temperature, water is a liquid.")
    if celsiusKelvin == "C" and temp > 100:
        print("At this tmeperature, water is a gas.")
    if celsiusKelvin == "K" and temp > 373:
        print("At this temperature, water is a gas.")
main()
