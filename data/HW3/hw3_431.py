KELVIN_TO_CELSIUS = 273.15
def main():
    temperature = float(input("Please enter the temperature: "))
    temp_scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if temp_scale == "K":
        temperature -= KELVIN_TO_CELSIUS
    if temperature >= 100:
        print ("At this temperature, water is a gas.")
    if temperature < 100 and temperature >= 0:
        print ("At this temperature, water is a liquid.")
    if temperature < 0:
        print ("At this temperature, water is a (frozen) solid.")
main()
