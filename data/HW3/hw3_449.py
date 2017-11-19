def main():
    temp =float(input("What is the temperature? "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        if temp <= 0:
            print("At this temperature, water is a solid.")
        if 0 < temp < 100:
            print("At this temperature, water is a liquid.")
        if temp >= 100:
            print("At this temperature, water is a gas.")
    if scale == "K":
        if temp <= 273.15:
            print("At this temperature, water is a solid.")
        if 273.15 < temp < 373.15:
            print("At this temperature, water is a liquid.")
        if temp >= 373.15:
            print("At this temperature, water is a gas.")
main()
