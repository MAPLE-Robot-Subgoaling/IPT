def main():
    print()
    scale = str(input("What scale? (C for Celsius; K for Kelvin) "))
    if((scale != "C") and (scale != "K")): 
        print("Your input was not correct. Start over.")
    else: 
        temperature = float(input("How many degrees? "))
        if scale == "C": 
            if temperature <= 0: 
                print("Water is a solid at this temperature.") 
            elif temperature >= 100: 
                print("Water is a gas at this temperature.") 
            else: 
                print("Water is a liquid at this temperature.") 
        else: 
            if temperature <= 273.15: 
                print("Water is a solid at this temperature.") 
            elif temperature >= 373.15: 
                print("Water is a gas at this temperature.") 
            else: 
                print("Water is a liquid at this temperature.") 
    print()
main()
