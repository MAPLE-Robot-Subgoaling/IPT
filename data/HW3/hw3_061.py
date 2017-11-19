def main():
    frozen = 32
    boil = 100
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    CONVERT = 273.15  
    if scale == "K":
        temp = temp - CONVERT
    if temp >= boil:
        print("At this temperature, water is a gas.")
    elif temp <= frozen:
        print("At this temperature, water is a (frozen) solid.")
    else:
        print("At this temperature, water is a liquid.")
main()
