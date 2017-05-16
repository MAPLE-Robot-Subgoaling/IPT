
def main():
    
    temp = float(input("Please enter the temperature:"))
    meas = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")

    if meas == "C" and temp <= 0:
        print("At this temperature, water is a (frozen) solid.")

    if meas == "C" and temp > 0 and temp < 100:
        print("At this temperature, water is a liquid.")

    if meas == "C" and temp >= 100:
        print("At this temperature, water is a gas.")

    if meas == "K" and temp <= 273.16:
        print("At this temperature, water is a (frozen) solid.")

    if meas == "K" and temp > 273.16 and temp < 373.16:
        print("At this temperature, water is a liquid.")

    if meas == "K" and temp >= 373.16:
        print("At this temperature, water is a gas.")

main()
