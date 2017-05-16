
def main():

    temp = float(input("Please enter a temperature:"))
    unit = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if unit == "C" and (temp <= 0):
        print("At this temperature, water is a (frozen) solid.")
    if unit == "C" and (temp < 100) and (temp > 0):
        print("At this temperature, water is liquid.")
    if unit == "C" and (temp > 100):
        print("At this temperature, water is a gas.")

    if unit == "K" and (temp <= 273):
        print("At this temperature, water is a (frozen) solid.")
    if unit == "K" and (temp > 273) and (temp < 373):
        print("At this temperature, water is liquid.")
    if unit == "K" and (temp > 373):
        print("At this temperature, water is a gas.")

        
    



main()
