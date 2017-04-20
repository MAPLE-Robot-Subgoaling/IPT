
def main():

    temp = float(input("Enter your temperature: "))
    system = input("Celcius (C) or Kelvin (K)? ")

    if system == "C":
        if temp<=0:
            print("Water is a solid.")
        elif temp<=100:
            print("Water is a liquid.")
        elif temp>100:
            print("Water is a gas.")
        else:
            print("Error on line 22.")

    elif system == "K":
        if temp<=273.15:
            print("Water is a solid.")
        elif temp <= 373.15:
            print("Water is a liquid.")
        elif temp >373.15:
            print("Water is a gas.")
        else:
            print("Error line 30.")

main()
