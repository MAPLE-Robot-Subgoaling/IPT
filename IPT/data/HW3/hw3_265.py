
def main():
    userTemp = float(input("Please enter the temperature:"))
    userScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    a = userTemp 
    
    if userScale == "C":
        if a > 0 and a < 100:
            print("At this temperature, water is a liquid.")
        elif a <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif a >= 100:
            print("At this temperature, water is a gas.")

    if userScale == "K":
        if a > 273 and a < 373:
            print("At this temperature, water is a liquid")
        elif a <= 273:
            print("At this temperature, water is a (frozen) solid.")
        elif a>= 373:
            print("At this temperature, water is a gas.")
main()
