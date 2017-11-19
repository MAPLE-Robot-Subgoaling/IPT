def main():
    state = ""
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        temp += 273.15
    if temp < 273.15:
        state = "(frozen) solid."
    elif temp < 373.15:
        state = "liquid."
    else:
        state = "gas."
    print("At this temperature, water is a", state)
main()
