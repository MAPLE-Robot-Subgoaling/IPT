

def main():
    userTemp = float(input("Please enter the temperature:"))
    unitsOfTemp = input("Please enter 'C' for Celsius or 'K' for Kelvin:")
    
    if unitsOfTemp == "C":
        print("The temperature is" , userTemp,"C")
        
        if userTemp  == float(0):
            print("At this temperature, water is a (frozen) solid.")
        if userTemp == float(100):
            print("At this temperature, water is a gas.")
        if float(0)< userTemp < float(100):
            print("At this temperature, water is a liquid.")
    
    elif unitsOfTemp == "K":
        print("The temperature is" , userTemp,"K")
    
        if userTemp == float(273.15):
            print("At this temperature, water is a (frozen) solid.")
        if userTemp == float(373.15):
            print("At this temperature, water is a gas.")
        if float(273.15)<userTemp < float(373.15):
            print("At this temperature, water is a liquid.")

main()
