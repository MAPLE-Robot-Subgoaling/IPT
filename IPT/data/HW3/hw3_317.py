
def main():
    FREEZING_POINT_C = 0
    BOILING_POINT_C = 100
    FREEZING_POINT_K = 273
    BOILING_POINT_K = 373.2

    temp = input("What is the temperature value?: ")
    temp = float(temp)
    units = input("Are the units Celsius (answer with C) or Kelvin (answer with K)?: ")

    if units == "C":
        if temp >= BOILING_POINT_C:
            print("Water is a gas at this temperature.")

        elif temp < BOILING_POINT_C and temp > FREEZING_POINT_C:
            print("Water is a liquid at this temperature.")

        else:
            print("Water is a solid at this temperature.")

    elif units == "K":

        if temp >= BOILING_POINT_K:
            print("Water is a gas at this temperature.")

        elif temp < BOILING_POINT_K and temp > FREEZING_POINT_K:
            print("Water is a liquid at this temperature.")

        else:
            print("Water is a solid at this temperature.")

main()
