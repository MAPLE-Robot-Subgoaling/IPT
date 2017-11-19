def main():
    print("Hello. This program will determine the physical state of water")
    print("based on the input temperature from the user.")
    FP_CELSIUS = 0
    BP_CELSIUS = 100
    FP_KELVIN = 273.15
    BP_KELVIN = 373.15
    temp = float(input("Please enter the temperature: "))
    unit = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if unit == "C":
        if temp <= FP_CELSIUS:
            print("At this temperature, water is a (frozen) solid.")
        elif FP_CELSIUS < temp <= BP_CELSIUS:
            print("At this temperature, water is a (liquidy) liquid.")
        else:
            print("At this temperature, water is a (gaseous) gas.")
    elif unit == "K":
        if temp <= FP_KELVIN:
            print("At this temperature, water is a (frozen) solid.")
        elif FP_KELVIN < temp <= BP_KELVIN:
            print("At this temperature, water is a (liquidy) liquid.")
        else:
            print("At this temperature, water is a (gaseous) gas.")
main()
