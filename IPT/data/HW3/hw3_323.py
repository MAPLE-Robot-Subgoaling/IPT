
def main ():

    inpTemp=float(input("What is the temperature?"))
    unit=input("What is the unit? (you may either enter C for Celcius or K for Kelvin)")


    if unit == "C":
        temp=inpTemp
    elif unit == "K":
        temp=inpTemp-273
    else: 
        print ("You did not enter a correct unit. Please either enter C for Celcius or K for Kelvin.")

    if temp >= 100:
        print ("Water is a gas at this temperature.")
    elif temp < 0:
        print ("Water is a solid at this temperature.")
    else:
        print ("Water is a liquid at this temperature.")

main ()

