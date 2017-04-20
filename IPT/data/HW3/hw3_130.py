
def main():
    temp = float(input("Please enter the temperature: "))
    scale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))

    if scale == "C":

        print(temp)
        if temp <= 0:
            print("The water is frozen.")
        elif temp > 0 and temp < 100:
            print("The water is liquid.")
        elif temp >= 100:
            print("The water is a gas (boiling).")

    elif scale == "K":

        print(temp)
        if temp == 0:
            print("The molecules have stopped moving.")
        elif temp > 0 and temp < 273.15:
            print("The water is frozen.")
        elif temp >= 273.15 and temp < 373.15:
            print("The water is liquid.")
        elif temp >= 373.15:
            print("The water is a gas (boiling).")
        elif temp < 0:
            print("error please enter a valid temperature.")

main()
    
