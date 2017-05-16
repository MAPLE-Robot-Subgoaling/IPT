
def main():
    KELVIN_BOILING = 373.16
    KELVIN_FREEZING = 273.16
    CELCUIS_BOILING = 100
    CELCIUS_FREEZING = 0
    temp = float(input("Please enter the temperature:"))
    unitOfMeasure = input("Please enter 'C' for Celcius or 'K' for Kelvin:")
    if (unitOfMeasure == "C"):
        if (temp <= CELCIUS_FREEZING):
            print("Water's a solid. Ice, Ice, Baby.")
        elif (temp >= CELCUIS_BOILING):
            print("Water's a gas. Turn off the tea pot!")
        else:
            print("Water's a liquid. Take a shower.")
    else:
        if (temp <= KELVIN_FREEZING):
            print("Water's a solid. Ice, Ice, Baby.")
        elif (temp >= KELVIN_BOILING):
            print("Water's a gas. Turn off the tea pot!")
        else:
            print("Water's a liquid. Take a shower.")
main()
