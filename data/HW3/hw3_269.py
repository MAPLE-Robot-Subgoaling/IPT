def main():
    degreeInput = float(input("Please enter the temperature: "))
    scaleInput = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if scaleInput == "C":
        if degreeInput >= 100:
            print("At this temperature, water is a gas.")
        elif degreeInput > 0:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a solid.")
    else:
        if degreeInput >= 373.15:
            print("At this temperature, water is a gas.")
        elif degreeInput > 273.15:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a solid.")
main()
