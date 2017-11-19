def main():
    temp = float(input("Please enter the temperature: "))
    units = input("Please enter 'K' for Kelvin or 'C' for Celcius: ")
    if (units == "K"):
        if  (temp <= 273):
            print("At this temperature, water is a solid.")
        if   ( temp >= 373):
            print("At this temperature,water is a gas.")
        if (temp < 373) and (temp > 273):
            print("At this temperature, water is a liquid.")
    if (units == "C"):
        if (temp <= 0):
            print ("At this temperature, water is a solid.")
        if (temp >= 100):
            print ("At this temperature, water is a gas.")
        if (temp < 100) and (temp > 0):
            print ("At this temperature, water is a liquid.")
main()
