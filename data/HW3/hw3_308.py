def main():
    temp = float(input("Please enter the temperature: "))
    measure = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if (measure == "C") and (temp <= 0):
        print("At this temperature, water is a (frozen) solid.")
    elif (measure == "C") and (0 < temp) and (temp < 100):
        print("At this temperture, water is a liquid.")
    elif (measure == "K") and (temp <= 273.15):
        print("At this temperature, water is a (frozen) solid.")
    elif (measure == "K") and (273.25 < temp) and (temp < 373.15):
        print("At this temperature, water is a liquid.")
    else: 
        print("At this temperature, water is a gas.")
main()
