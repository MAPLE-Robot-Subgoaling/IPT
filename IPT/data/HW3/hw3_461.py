
def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if scale == 'C':    
        if temp <= 0 :
            print("At ", temp, " Celsius, water is a solid.")
        elif temp > 0 and temp < 100:
            print("At ", temp, " Celsius, water is a liquid.")
        else:
            print("At ", temp, " Celsius, water is a gas.")
    else:
        if temp <= 273 :
            print("At ", temp, " Kelvin, water is a solid.")
        elif temp > 273 and temp < 373:
            print("At ", temp, " Kelvin, water is a liquid.")
        else:
            print("At ", temp, " Kelvin, water is a gas.")
main()
