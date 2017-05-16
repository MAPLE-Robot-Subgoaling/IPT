
def main():

    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")

    if scale == "C" and temp < 0:
        print("At this temperature, water is frozen.")
    elif scale == "C" and temp > 100:
        print("At this temperature, water is a gas.")
    elif scale == "C":
        print("At this temperature, water is liquid.")

    if scale == "K" and temp < 273.15:
        print("At this temperature, water is frozen.")
    elif scale == "K" and temp > 373.15:
        print("At this temperature, water is a gas.")
    elif scale == "K":
        print("At this temperature, water is liquid.")
main()
