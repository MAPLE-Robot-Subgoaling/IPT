def main():
    temp = float(input("Please enter the tempurature:"))
    inKelvin = input("Please enter 'C' for Celsius, or 'K for Kelvin:") == "K"
    if not inKelvin:
        temp += 273.15
    if temp <= 273.15:
        state = "(frozen) solid"
    elif temp >= 373.15:
        state = "gas"
    else:
        state = "liquid"
    print("At this tempurature, water is a", state)
main()
