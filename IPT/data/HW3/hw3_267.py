
KELVIN = "K"
CELCIUS = "C"
KELVIN_DIFFERENCE = 273.15
FREEZING_POINT = 0
def main():
    temperature= float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    if (scale == KELVIN):
        temperature -= KELVIN_DIFFERENCE
    if(temperature <= FREEZING_POINT):
        print("At this temperature, water is solid.")
    elif(temperature < 100):
        print("At this temperature, water is a liquid.")
    else:
        print("At this temperature, water is a gas.")
main()
