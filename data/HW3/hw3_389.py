def main():
    KELVIN = 273 
    temperature = float(input("Please enter the temperature: ")) 
    scale = KELVIN if input("Please enter C for Celsius, or 'K' for Kelvin: ") == "K" else 0 
    if temperature - scale > 100:
        print("At this temperature, water is a gas") 
    elif temperature - scale > 0:
        print("At this temperature, water is a liquid") 
    else:
        print("At this temperature, water is a (frozen) solid") 
main()