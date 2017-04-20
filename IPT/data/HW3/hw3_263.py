
def main():

    temperature = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    
    if scale == 'C':
        if temperature <= 0:
            print("At this temperature, water is a solid.")
        elif 0 < temperature < 100:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    
    else:
        if temperature <= 273:
            print("At this temperature, water is a solid.")
        elif 273 < temperature < 373:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")

main()
