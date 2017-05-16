
def main():

    userTemp = float(input("Please enter a temperature: "))
    tempType = input("Is your temperature in Celsius or Kelvin? Please type either 'C' for Celsius or 'K' for Kelvin: ")

    CELS_FP = 0
    CELS_BP = 100
    KELV_FP = 273.15
    KELV_BP = 373.15
    
    if tempType == "C":
        if userTemp <= CELS_FP:
            print("At this temperature, water is a solid.")
        elif userTemp < CELS_BP:
            print("At this temperature, water is a liquid.")
        elif userTemp >=CELS_BP:
            print("At this temperature, water is a gas.")
    else:
        if userTemp <= KELV_FP:
            print("At this temperature, water is a solid.")
        elif userTemp < KELV_BP:
            print("At this temperature, water is a liquid.")
        elif userTemp >= KELV_BP:
            print("At this temperature, water is a gas.")



main()
