def main():
    temp = float(input("Please enter the temperature: "))
    COrK = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if COrK == "C":
        if temp > 100:
            print("At this temperature, water is a gas.")
        elif temp <=100 and temp > 0:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a solid.")
    if COrK == "K":
        if temp > 373:
            print("At this temperature, water is a gas.")
        elif temp <=373 and temp > 273:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a solid.")
main()
