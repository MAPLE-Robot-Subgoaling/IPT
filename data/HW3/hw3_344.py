def main():
    temp = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if tempScale == "K" :
        temp = (temp - 273.15)
    if temp <= 0.0:
        print("At this temperature, water is a (frozen) solid.")
    elif temp >= 100:
        print("At this temperature, water is a gas.")
    else:
        print("At this temperature, water is a liquid.")
main()
