
def main():
    
    waterTemp = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    if tempType == "K":
        waterTemp = float(waterTemp - 273.15)
    
    if waterTemp <= 0:
        print("At this temperature, water is a (frozen) solid.")
    elif waterTemp >= 100:
        print("At this temperature, water is a gas.")
    else:
        print("At this temperature, water is a liquid.")


main()
