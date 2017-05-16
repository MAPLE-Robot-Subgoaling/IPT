
def main():

    temp = float(input("Please enter a temperature " ))
    unit = input("Is your temperature in Celsius (C) or Kelvin (K)? " )
    CONVERSION = 273.15

    if unit == "K":
        tempCelsius = temp - CONVERSION
        if tempCelsius <= 0:
            print("At your temperature, water is a solid.")
        elif tempCelsius >= 100:
            print("At your temperature, water is a Gas.")
        else:
            print("At your temperature, water is a liquid.")

    elif unit == "C":
        if temp <= 0:
            print("At your temperature, water is a solid.")
        elif temp >= 100:
            print("At your temperature, water is a Gas.")
        else:
            print("At your temperature, water is a liquid.")

main()
