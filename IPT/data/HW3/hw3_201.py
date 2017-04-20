

def main():
    
    temperature = float(input("Please enter the temperature: "))
    unit = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
               
    
    if unit == "C": 
        if (temperature > 0 and temperature < 100):
            print("At this temperature, water is a liquid.")
        elif (temperature < 0):
            print("At this temperature, water is a (frozen) solid.")
        else :
            print("At this temperature, water is a gas.")

    elif unit == "K": 
        if temperature > 273 and temperature < 373:
            print("At this temperature, water is a liquid.")
        elif temperature < 273:
            print("At this temperature, water is a (frozen) solid.")
        else: 
            print("At this temperature, water is a gas.")



main()
