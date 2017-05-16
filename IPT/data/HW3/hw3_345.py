
def main():
    temp = int(input("Please enter the temperature: "))
    measure = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if((measure == "C") and (temp >= 100)):
        print("At this temperature, water is a gas.")
    elif((measure == "C") and (temp > 0) and (temp < 100)):
        print("At this temperature, water is a liquid.")
    elif((measure == "C") and (temp < 0)):
        print("At this temperature, water is a (frozen) solid.")
    elif((measure == "K") and (temp <= 373)):
        print("At this temperature, water is a gas.")
    elif((measure == "K") and (temp <= 273) and (temp > 373)):
        print("At this temperature, water is a liquid.")
    elif((measure == "K") and (temp > 273)):
        print("At this temperature, water is a (frozen) solid.")

    
        
     
main()
