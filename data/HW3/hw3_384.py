def main():
    CELSIUS_HIGH = float("100")
    CELSIUS_LOW  = float("0")
    KELVIN_HIGH  = float("372.5")
    KELVIN_LOW   = float("0")
    tempInput = float(input("Please enter the temperature: "))
    unitInput = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if unitInput == "K":
        if tempInput >=  KELVIN_HIGH:
            print("Your water is now gas!")
        elif tempInput <= KELVIN_LOW:
            print("Your water is now solid!")
        elif KELVIN_LOW < tempInput < KELVIN_HIGH:
            print("Your water is now liquid!")
    elif unitInput == "C":
        if tempInput >= CELSIUS_HIGH:
            print("Your water is now gas!")
        elif tempInput <= CELSIUS_LOW:
            print("Your water is now solid!")
        elif CELSIUS_LOW < tempInput < CELSIUS_HIGH:
            print("Your water is now liquid!")
main()
