def main():
    Temp = float(input("What is the temperature. "))
    scale = input("please enter 'C' for Celsius or 'K' for Kelvin ")
    if scale == "K":
        Temp = Temp - 273
    if Temp > 100:
        print("Pure water is a gas at this temperature")
    elif Temp < -273:
        print("You have frozen the universe.  congratulations.")
    elif Temp < 0:
        print("Pure water is frozen at that temperature.")
    else:
        print("Pure water is a liquid at that temperature.")
main()
