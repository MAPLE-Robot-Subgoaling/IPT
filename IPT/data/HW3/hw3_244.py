
def main():

    temperature=float(input("Please enter the temperature: "))

    scale=str(input("Please enter 'C' for Celcius, or 'K' for Kelvin: "))

    if scale=='k':
        temperature=(temperature-273.15)
    
    if temperature>=100:
        print("At this temperature, water is a gas.")
    elif temperature>0:
        print("At this temperature, water is a liquid.")
    else:
        print("At this temperature, water is a solid.")

main()

