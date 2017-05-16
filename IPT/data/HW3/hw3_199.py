
def main():

    print()

    scale = str(input("What scale? (C for Celsius; K for Kelvin) "))

    if((scale != "C") and (scale != "K")): #When scale is not defined as C or K, it tells the user to start over, because any other value will not work with the program.
        print("Your input was not correct. Start over.")

    else: #When the user enters the correct scale (C or K)
        temperature = float(input("How many degrees? "))
        if scale == "C": #When the user enters C
            if temperature <= 0: #Freezing point at 0 degrees Celcius.
                print("Water is a solid at this temperature.") #Solid
            elif temperature >= 100: #Boiling point at 100 degrees Celcius.
                print("Water is a gas at this temperature.") #Gas
            else: #Not freezing or boiling
                print("Water is a liquid at this temperature.") #Liquid
        else: #When the user enters K
            if temperature <= 273.15: #Freezing point at 273.15 degrees Celcius
                print("Water is a solid at this temperature.") #Solid
            elif temperature >= 373.15: #Boiling point at 373.15 degrees Kelvin
                print("Water is a gas at this temperature.") #Gas
            else: #Not freezing or boiling
                print("Water is a liquid at this temperature.") #Liquid

    print()

main()


