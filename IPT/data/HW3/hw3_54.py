def main():
    temp = float(input("Please enter the temperature:"))
    tempType = input("Please enter 'C' for Celsius or 'K' for Kelvin:")
    if (tempType== 'C' and temp <=0) or (tempType == 'K' and temp <= 273):
        print("At this temperature, the water is a solid.")
    elif(tempType== 'C' and temp >100) or (tempType == 'K' and temp > 373):
        print("At this temperature, the water is a gas.")
    else:
        print("At this temperature, the water is a liquid.")
main()
