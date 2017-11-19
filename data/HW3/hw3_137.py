def main():
    temp = float(input("Enter the temperature : "))
    scale = input("Enter 'C' for celcius or 'K' for Kelvin : ")
    if scale == "C":
        if temp <= 0:
            print("The water is frozen solid.")
        if temp > 0 and temp < 100:
            print("The water is still a liquid")
        if temp >= 100:
            print("The water is now a gas.")
    if scale == "K":
        if temp <= 0:
            print("The water is frozen solid.")
        if temp > 0 and temp < 373.15:
            print("The water is still a liquid.")
        if temp >= 373.15:
            print("The water is a gas.")
main()
