def main():
    temp = float(input("Please enter the temperature:  "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin:  ")
    if scale == "K":
        temp = temp - 273.16
    if temp < 0:
        state = "(frozen) solid"
    elif temp < 100:
        state = "liquid"
    else:
        state = "gas"
    print("At this temperature, water is a " + state + ".")
main()
