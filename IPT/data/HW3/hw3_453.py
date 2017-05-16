
def main():
    KELVIN = 273 # Add 273 to celsius amount for Kelvin
    temperature = float(input("Please enter the temperature: ")) # ask user for temperature
    scale = KELVIN if input("Please enter C for Celsius, or 'K' for Kelvin: ") == "K" else 0 # ask user for scale
    if temperature - scale > 100:
        print("At this temperature, water is a gas") # >100C (373K)
    elif temperature - scale > 0:
        print("At this temperature, water is a liquid") # 0-100C (273-373K)
    else:
        print("At this temperature, water is a (frozen) solid") # <0C (273K)
        
main()