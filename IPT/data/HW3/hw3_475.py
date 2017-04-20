

def main() :

    temp = float(input("What is the temperature?"))
    unit = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin:"))
    
    if unit == "C" and temp > 0 and temp <100:
        print("The water is a liquid.")
        
    if unit == "C" and temp > 100:
        print("The water is a gas.")

    if unit == "C" and temp < 0:
        print("The water is a solid (frozen).")

    if unit == "K" and temp < 273:
        print("The water is a solid (frozen).")

    if unit == 'K' and temp > 273 and temp < 373:
        print("The water is a liquid.")

    if unit == "K" and temp > 373:
        print("The water is a gas.")

main()
