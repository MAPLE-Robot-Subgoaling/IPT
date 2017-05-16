
def main():

    userTemp = float(input(" Please enter the tempaerature: "))
    tempCK = input(" Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if (tempCK == "C") and (userTemp <= 32):
        print("At this temperature water is a (frozen) solid")
    elif (tempCK == "C") and (32 < userTemp < 100):
        print(" At this temperature water is a liquid")
    elif (tempCK == "C") and (userTemp > 100):
        print(" At this temperature water is a gas")
    elif (tempCK == "K") and (userTemp <= 305.15):
        print("At this temperature water is a (frozen) solid")
    elif (tempCK == "K") and (305.15 < userTemp < 373.15):
        print("At this temperature water is a liquid")
    elif (tempCK == "K") and (userTemp > 373.15): 
        print("At this tempearature water is a gas")
main()
