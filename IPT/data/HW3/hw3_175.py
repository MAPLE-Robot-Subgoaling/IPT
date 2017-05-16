SOLIDC=0
GASC=100
SOLIDK=273.16
GASK=373.16
def main():
      
    Temp=float(input("Please enter the temperature:"))
    Scale=input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    
    if Scale=="C":
        if Temp<=SOLIDC:
            print("At this temperature, water is a (frozen) solid.")
        elif Temp>=GASC:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    elif Scale=="K":
        if Temp<=SOLIDK:
            print("At this temperature, water is a (frozen) solid.")
        elif Temp>=GASK:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        print("You did not enter a valid scale")

main()
