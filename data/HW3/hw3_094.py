def main():
    temp = 0.0
    tempType = ""
    temp = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if(tempType == "C"):
        if(temp <= 0):
            print("At this temperature, water is a solid.")
        elif(temp >= 100):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        if(temp >= 373.16):
            print("At this temperature, water is a gas.")
        elif(temp <= 273.16):
            print("At this temperature, water is a solid.")
        else:
            print("At this temperature, water is a liquid.")
main()
