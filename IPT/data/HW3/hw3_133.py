def main():
    temp = float(input("Please enter your temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C" and temp >= 100:
        print("At this temperature, the water is a gas.")          
    elif scale == "C" and (temp <100 and temp >0):
        print("At this temperature, the water is a liquid.")
    elif scale == "C" and temp <0:
        print("At this temperature, the water is a solid.")

    if scale == "K" and temp >= 373.16:
        print("At this temperature, the water is a gas.")
    elif scale == "K" and (temp < 373.16 and temp > 273.16):
        print("At this temperature, the water is a liquid.")
    elif scale == "K" and temp < 273.16:
        print("At this temperature, the water is a solid.")
main()
