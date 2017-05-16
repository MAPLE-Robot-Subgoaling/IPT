
def main():

    waterTemp = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if tempScale == "C":
        if waterTemp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        if waterTemp > 0 and waterTemp < 100:
            print("At this temperature, water is a liquid.")
        if waterTemp >= 100:
            print("At this temperature, water is a gas.")

    if tempScale == "K":
        if waterTemp <= 273.15:
            print("At this temperature, water is a (frozen) solid.")
        if waterTemp > 273.15 and waterTemp < 373.15:
            print("At this temperature, water is a liquid.")
        if waterTemp >= 373.15:
            print("At this temperature, water is a gas.")

main()
