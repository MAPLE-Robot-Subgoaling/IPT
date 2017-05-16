
def main():
    temp1 = float(input("Please enter the temperature: "))
    scale1 = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale1 == "C":
        if temp1 <= 0:
            print("At this temperature, water is a solid.")
        elif temp1 >= 100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    if scale1 == "K":
        if temp1 <= 273:
            print("At this temperature, water is a solid.")
        elif temp1 >= 373:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")

main()
