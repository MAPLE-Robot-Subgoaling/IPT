
def main():
    
    tempScale = input("Enter 'C' to use the Celsius scale, or 'K' to use the Kelvin scale. ")
    temp = float(input("What is the temperature? "))

    if tempScale == 'C' and temp < 0:
        print("Water is a solid.")

    elif tempScale == 'C' and 100 > temp >= 0:
        print("Water is a liquid.")

    elif tempScale == 'C' and temp >= 100:
        print("Water is a gas.")

    elif tempScale == 'K' and temp < 273.2:
        print("Water is a solid.")

    elif tempScale == 'K' and 273.2 <= temp < 373.2:
        print("Water is a liquid.")

    else:
        print("Water is a gas.")

main()
