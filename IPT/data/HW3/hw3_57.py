
def main():
    
    waterTemp = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")


    if tempScale == 'C':
        if waterTemp >= 100:
            print("At this temperature, water is a gas.")
        elif waterTemp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")

    elif tempScale == 'K':
        if waterTemp >= 373:
            print("At this temperature, water is a gas.")
        elif waterTemp <= 273:
            print("At this temperature, water is a (frozen) solid.")
        else: 
            print("At this temperature, water is a liquid.")

    
        
            

    




main ()
