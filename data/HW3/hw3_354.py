def main():
    temp = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if (tempScale == "C") and (temp < 0):
        print("At this temperature, water is a (frozen) solid.")
    if (tempScale == "K") and (temp < 273.15):
        print("At this temperature, water is a (frozen) solid.")
    if (tempScale == "C") and (0 <= temp < 100):
        print("At this temperature, water is a liquid.")
    if (tempScale == "K") and (273.15 <= temp < 373.15):
        print("At this temperature, water is a liquid.")
    if (tempScale == "C") and (temp >= 100):
        print("At this temperature, water is a gas.")
    if (tempScale == "K") and (temp >= 373.15):
        print("At this temperature, water is a gas.")
main()
