
def main():
    KELVIN = "K"
    CELSIUS = "C"
    BOIL = float(373)     # Water's boiling point in Kelvin
    FREEZE = float(273)   # Water's freezing point in Kelvin
    
    temperature = float(input("Please enter the temperature: "))
    unit = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    
    if unit == CELSIUS:
        temperature = temperature + FREEZE
        unit = KELVIN
    if unit == KELVIN:
        if temperature < 0:
            print("At this temperature, water is impossibly cold.")
        elif 0 <= temperature < FREEZE:
            print("At this temperature, water is a (frozen) solid.")
        elif temperature == FREEZE:
            print("At this temperature, water is in the process of freezing or melting.")
        elif FREEZE < temperature < BOIL:
            print("At this temperature, water is a liquid.")
        elif temperature == BOIL:
            print("At this temperature, water is in the process of boiling or condensing.")
        elif temperature > BOIL:
            print("At this temperature, water is a gas.")
        
main()
