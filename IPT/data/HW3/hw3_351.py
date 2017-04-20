
def main():
   
    oneInput= 0
    temp= (float(input("Please enter the Temperature")))
    tempOutput=input("Please enter 'C' for Celsius, or 'K' for Kelvin:")

    while tempOutput== "C" and oneInput < 1:
       
        oneInput= oneInput + 1

        if temp < 0:
            print("The water is frozen solid")
        
        elif temp > 0 and temp < 100:
            print ("The water is a liquid")

        else:
            print("The water is in gas form")

    while tempOutput== "K"and oneInput < 1:
        oneInput= oneInput + 1

        if temp < 273:
            print("The water is frozen solid")

        elif temp > 273 and temp < 373:
            print("The water is a liquid")
            
        else:
            print("The water is in gas form")
main()
