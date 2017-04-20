
def main():

    temperature = float(input(" Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsuis, or 'K' for Kelvin: ")


    if tempType == "K" and temperature> 373: 
        print("At this temperature, the water is gas") 
    if tempType == "K" and   373 >temperature>273: 
        print("At this temperature, the water is liquid")
    if tempType == "K" and temperature < 273: 
        print("At this temperature, the water is soild")

    if tempType == "C" and temperature> 100: 
        print("At this temperature, the water is gas")
    if tempType == "C" and 100>temperature>0: 
        print("At this temperature, the water is liquid") 
    if tempType == "C" and temperature< 0: 
        print("At this temperature, the water is solid")







main()
